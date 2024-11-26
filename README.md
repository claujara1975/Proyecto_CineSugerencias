🌟 Proyecto_CineSugerencias 🌟
Proyecto Individual Nº1: Machine Learning Operations (MLOps)
¡Bienvenidos a Proyecto_CineSugerencias! 🎬 Este es el primer proyecto de la etapa de Labs, donde asumo el rol de MLOps Engineer. Llevo a cabo el ciclo completo para construir un sistema de recomendación de películas, desde la preparación de datos hasta el desarrollo y despliegue de una API funcional usando FastAPI.

📌 Objetivo: Crear un sistema que ofrezca recomendaciones personalizadas y pueda ser consumido por otros equipos en una start-up que agrega plataformas de streaming.

🧐 Contexto y Descripción del Problema
Como nuevo integrante de una start-up, enfrenté el desafío de desarrollar un sistema de recomendación para películas a partir de datos sin procesar. Estos datos presentaban estructuras anidadas y valores faltantes.

🔧 En este proyecto, mi tarea fue realizar ingeniería de datos y crear un Minimum Viable Product (MVP) en un plazo limitado.

🔍 Rol a Desarrollar
Para transformar los datos desde su estado bruto hasta una estructura lista para análisis y modelado, abordé las siguientes fases:

⚙ ETL (Extract, Transform, Load)
📊 Análisis Exploratorio de Datos (EDA)
🚀 Modelado y despliegue de la API de recomendaciones
📑 Propuesta de Trabajo
🔄 Transformaciones Realizadas
Para preparar los datos de manera rápida y efectiva, se realizaron las siguientes transformaciones:

🗂️ Desanidado de campos complejos:
Columnas como belongs_to_collection y production_companies fueron desanidadas para optimizar consultas en la API.
⚠ Manejo de valores nulos:
Rellené valores nulos de revenue y budget con 0.
Eliminé filas con valores nulos en release_date.
📅 Formato de fechas:
Convertí fechas al formato AAAA-mm-dd y extraje el año de lanzamiento en la columna release_year.
💰 Cálculo de Retorno de Inversión:
Creé la columna return calculando revenue / budget, asignando 0 cuando no hay datos.
🗑️ Eliminación de columnas innecesarias:
Columnas como video, imdb_id, adult, original_title, poster_path y homepage fueron eliminadas para simplificar el dataset.
🌐 Desarrollo de la API
Utilicé FastAPI para disponibilizar los datos transformados mediante endpoints clave:

cantidad_filmaciones_mes(mes):
Devuelve la cantidad de películas estrenadas en un mes dado.

cantidad_filmaciones_dia(dia):
Devuelve la cantidad de películas estrenadas en un día específico.

score_titulo(titulo_de_la_filmación):
Devuelve título, año de estreno y score de popularidad de una película.

votos_titulo(titulo_de_la_filmación):
Devuelve cantidad de votos y promedio de puntuación de una película (si tiene al menos 2000 valoraciones).

get_actor(nombre_actor):
Devuelve el éxito del actor mediante retorno total, cantidad de películas y promedio de retorno por película.

get_director(nombre_director):
Devuelve el éxito del director mostrando retorno, fecha de lanzamiento y ganancias de cada película.

🤖 Sistema de Recomendación
El sistema de recomendación utiliza técnicas de similitud para sugerir cinco películas similares a la ingresada por el usuario, ordenadas por score de similaridad.

🔑 Endpoint:

recomendacion(titulo):
Devuelve una lista de cinco películas recomendadas, en orden descendente de similitud.
📈 Análisis Exploratorio de Datos (EDA)
El análisis incluyó:

Identificación de outliers.
Análisis de correlaciones.
Visualizaciones como nubes de palabras para comprender la distribución de títulos y patrones en los datos.
📊 Este análisis proporciona una base sólida para el modelo de recomendación.

🚀 Despliegue
El proyecto se desplegó en Render.

🌐 La API es accesible en línea y su funcionalidad se demuestra en un video de 7 minutos que resume las consultas y el modelo de recomendaciones.
🎥 Video Demostrativo:
Puedes acceder al video en este enlace: Demostración del Proyecto.

📝 Criterios de Evaluación
✔ Código: Prolijo, organizado y comentado. Uso adecuado de funciones y clases.
✔ Repositorio: Archivos organizados y un README detallado.
✔ MVP Completo: Transformaciones y requerimientos cumplidos con un sistema funcional.

📂 Datos Utilizados
movies_dataset.parquet
credits.parquet
📖 El proyecto incluye un diccionario de datos para facilitar la comprensión de las columnas.

🎉 ¡Gracias por revisar Proyecto_CineSugerencias! Espero que este sistema de recomendaciones sea útil y eficiente.
