# Importación de librerías 
from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Inicialización de la aplicación con título y descripción
app = FastAPI(
    title="API de Consulta y Recomendación de Películas",
    description="API para consultar información sobre películas y recibir recomendaciones basadas en similitud."
)

# Cargar los datasets en memoria
# Definir las rutas de los archivos
ruta_movies = 'Datasets/movies_df.parquet'
ruta_crew = 'Datasets/crew_df.parquet'
ruta_cast = 'Datasets/cast_df.parquet'


# Cargar los archivos Parquet en DataFrames
movies_df = pd.read_parquet(ruta_movies)
crew_df = pd.read_parquet(ruta_crew)
cast_df = pd.read_parquet(ruta_cast)


# Ruta de inicio
@app.get("/", tags=['home'])
async def index():
    return {"message": "¡Bienvenid@ a la API para consultar y recibir recomendaciones de películas! Para más información, visite /docs."}

# Ruta de información sobre la API y el proyecto
@app.get("/about")
async def about():
    return {
        "autor": "Claudia Jara Yañez",
        "fecha": "Noviembre de 2024",
        "proyecto": "PROYECTO INDIVIDUAL Nº1: Machine Learning Operations (MLOps)"
    }


# Ruta de cantidad de filmaciones para un determinado mes
@app.get("/cantidad_filmaciones_mes/{mes}", name="Cantidad filmaciones (mes)")
async def cantidad_filmaciones_mes(mes: str):

    # Diccionario de meses para convertir nombres en números de mes
    meses = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4,
        'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
        'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }
    
    # Convertir el nombre del mes a número
    mes_numero = meses.get(mes.lower())
    
    if mes_numero is None:
        return "Mes no válido. Por favor, ingresa un mes en español."
    
    # Asegurarse de que la columna 'release_date' sea de tipo datetime
    if not pd.api.types.is_datetime64_any_dtype(movies_df['release_date']):
        movies_df['release_date'] = pd.to_datetime(movies_df['release_date'], errors='coerce')
    
    # Filtrar las filas que coincidan con el mes y que tengan una fecha válida
    cantidad = movies_df[movies_df['release_date'].dt.month == mes_numero].shape[0]
    return f"{cantidad} películas fueron estrenadas en el mes de {mes.capitalize()}"



# Ruta de cantidad de filmaciones para un determinado día de la semana
@app.get("/cantidad_filmaciones_dia/{dia}", name="Cantidad filmaciones (día)")
async def cantidad_filmaciones_dia(dia: str):
    
    # Diccionario de días para convertir nombres en números de días
    dias = {
        'lunes': 0, 'martes': 1, 'miercoles': 2, 'jueves': 3,
        'viernes': 4, 'sabado': 5, 'domingo': 6
    }
    
    dia_numero = dias.get(dia.lower())
    
    if dia_numero is not None:
        cantidad = movies_df[movies_df['release_date'].dt.dayofweek == dia_numero].shape[0]
        return f"{cantidad} películas fueron estrenadas en los días {dia.capitalize()}"
    else:
        return "Día no válido. Por favor, ingresa un día de la semana en español."



# Ruta de búsqueda por título
@app.get("/score_titulo/{titulo}", name="Score de una filmación")
async def score_titulo(titulo: str):
    pelicula = movies_df[movies_df['title'].str.lower() == titulo.lower()]
    
    if not pelicula.empty:
        pelicula_info = pelicula.iloc[0]
        return f"Título: {pelicula_info['title']}, Año de Estreno: {pelicula_info['release_date'].year}, Score de Popularidad: {pelicula_info['popularity']}"
    else:
        return "Película no encontrada."



# Ruta de cantidad de votos para una determinada película
@app.get("/votos_titulo/{titulo}", name="Cantidad de votos de una filmación")
async def votos_titulo(titulo: str):
    pelicula = movies_df[movies_df['title'].str.lower() == titulo.lower()]
    
    if not pelicula.empty:
        cantidad_votos = pelicula['vote_count'].values[0]
        valor_promedio = pelicula['vote_average'].values[0]
        
        if cantidad_votos >= 2000:
            return f"Título: {titulo}, Cantidad de Votos: {cantidad_votos}, Valor Promedio: {valor_promedio}"
        else:
            return "La película no cumple con el mínimo de 2000 votos."
    else:
        return "Película no encontrada."



# Ruta de búsqueda por actor
# Asegúrate de que ambos DataFrames tengan la columna 'id' como tipo int64
cast_df['id'] = cast_df['id'].astype(int)
movies_df['id'] = movies_df['id'].astype(int)
@app.get("/get_actor/{nombre_actor}", name="Búsqueda por actor")
async def get_actor(nombre_actor: str):
    # Normalizar el nombre del actor
    nombre_actor = nombre_actor.strip().lower()
    
    # Filtrar el DataFrame de cast para obtener solo los registros del actor especificado
    actor_movies = cast_df[cast_df['cast_name'].str.strip().str.lower() == nombre_actor]
    
    # Verificar si el actor tiene registros
    if actor_movies.empty:
        return {"error": f"El actor {nombre_actor.title()} no se encuentra en el dataset."}
    
    # Obtener la cantidad de películas en las que ha participado
    cantidad_peliculas = actor_movies.shape[0]
    
    # Unir con movies_df para obtener el retorno total
    peliculas_con_revenue = actor_movies.merge(movies_df[['id', 'revenue']], on='id', how='left')
    
    # Calcular el retorno total excluyendo directores
    retorno_total = peliculas_con_revenue['revenue'].sum() if 'revenue' in peliculas_con_revenue else 0
    
    # Calcular el promedio de retorno por película
    promedio_retorno = retorno_total / cantidad_peliculas if cantidad_peliculas > 0 else 0
    
    # Formatear el resultado como un diccionario
    if True:
        return (f"El actor {nombre_actor.title()} ha participado de {cantidad_peliculas} filmaciones, "
                f"con un retorno total de {retorno_total} y un promedio de {promedio_retorno} por filmación.")



# Ruta de búsqueda por director
@app.get("/get_director/{nombre_director}", name="Búsqueda por director")
async def get_director(nombre_director: str):
    # Filtrar crew_df para obtener solo las filas del director especificado
    director_movies = crew_df[
        (crew_df['crew_name'].str.strip().str.lower() == nombre_director.lower()) &
        (crew_df['crew_job'].str.strip().str.lower() == 'director')
    ]

    # Verificar si el director tiene registros
    if director_movies.empty:
        return f"No se encontraron registros para el director: {nombre_director}"

    # Obtener el ID de las películas que dirigió el director
    movie_ids = director_movies['id'].unique()

    # Filtrar las películas de movies_df basadas en los IDs de las películas en crew_df
    director_movies_details = movies_df[movies_df['id'].isin(movie_ids)]

    # Calcular el retorno total y el número de películas
    total_return = director_movies_details['return'].sum()
    number_of_movies = director_movies_details.shape[0]
    average_return_per_movie = total_return / number_of_movies if number_of_movies > 0 else 0

    # Formatear el retorno para que se vea más limpio
    total_return_rounded = round(total_return, 2)
    average_return_rounded = round(average_return_per_movie, 2)

    # Mensaje de salida personalizado
    return f"El director {nombre_director} ha conseguido un retorno total de {total_return_rounded:.2f} con un promedio de {average_return_rounded:.2f} por filmación."



# Machine Learning

# Ruta de recomendación de películas
@app.get('/recomendacion/{titulo}', name="Sistema de recomendación")
async def recomendacion(titulo, movies_df):
    """Se ingresa el nombre de una película y se recomienda las 5 películas más similares en una lista"""
    
    # Obtener las columnas reales y comparar
    available_columns = movies_df.columns.tolist()
    
    # Definir las columnas de géneros que esperas encontrar
    expected_genres = ['Action', 'Adventure', 'Animation', 'Comedy']
    genre_columns = [genre for genre in expected_genres if genre in available_columns]
    
    # Validar que haya columnas de géneros en el DataFrame
    if not genre_columns:
        return "Error: No se encontraron columnas de géneros en el DataFrame."
    
    # Seleccionar solo las columnas de géneros presentes
    movies_df_genres = movies_df[genre_columns]
    
    # Verificar que la película existe en el DataFrame
    if titulo not in movies_df['title'].values:
        return "Película no encontrada"
    
    # Obtener el índice de la película en el DataFrame
    idx = movies_df.index[movies_df['title'] == titulo][0]
    
    # Calcular la similitud coseno entre las películas basadas en los géneros
    similitud = cosine_similarity([movies_df_genres.iloc[idx]], movies_df_genres)[0]
    
    # Seleccionar los índices de las 5 películas más similares, excluyendo la película de entrada
    similares = sorted(list(enumerate(similitud)), key=lambda x: x[1], reverse=True)[1:6]
    recomendaciones = [movies_df.iloc[i[0]]['title'] for i in similares]
    
    return {'lista recomendada': recomendaciones}
