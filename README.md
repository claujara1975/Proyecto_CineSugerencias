# Proyecto_CineSugerencias

**Proyecto Individual Nº1: Machine Learning Operations (MLOps)**

¡Bienvenidos a **Proyecto_CineSugerencias**! Este es el primer proyecto de la etapa de Labs, en el cual asumo el rol de **MLOps Engineer**. Llevo a cabo el ciclo completo para construir un sistema de recomendación de películas, desde la preparación de datos hasta el desarrollo y despliegue de una API funcional usando FastAPI. El objetivo es crear un sistema que ofrezca recomendaciones personalizadas y pueda ser consumido por otros equipos en una start-up que agrega plataformas de streaming.

## Contexto y Descripción del Problema

Como nuevo integrante de una start-up, enfrenté el desafío de desarrollar un sistema de recomendación para películas a partir de datos sin procesar. Estos datos presentaban estructuras anidadas y valores faltantes. En este proyecto, mi tarea fue realizar ingeniería de datos y crear un Minimum Viable Product (MVP) en un plazo limitado.

### Rol a Desarrollar
He abordado las siguientes fases para transformar los datos desde su estado bruto hasta una estructura lista para análisis y modelado:
- **ETL** (Extract, Transform, Load)
- **Análisis Exploratorio de Datos (EDA)**
- **Modelado y despliegue de la API de recomendaciones**

## Propuesta de Trabajo

### Transformaciones Realizadas
Para preparar los datos de manera rápida y efectiva, se realizaron las siguientes transformaciones:
- **Desanidado de campos complejos**: Desanidé columnas como `belongs_to_collection` y `production_companies` para optimizar consultas en la API.
- **Manejo de valores nulos**:
  - Rellené valores nulos de `revenue` y `budget` con 0.
  - Eliminé filas con valores nulos en `release_date`.
- **Formato de fechas**: Convertí fechas al formato `AAAA-mm-dd` y extraje el año de lanzamiento en la columna `release_year`.
- **Cálculo de Retorno de Inversión**: Creé la columna `return` que calcula `revenue / budget`, asignando 0 cuando no hay datos.
- **Eliminación de columnas innecesarias**: Eliminé columnas como `video`, `imdb_id`, `adult`, `original_title`, `poster_path`, y `homepage` para simplificar el dataset.

### Desarrollo de la API
Utilicé **FastAPI** para disponibilizar los datos transformados mediante endpoints clave. Las funciones implementadas son:

1. `cantidad_filmaciones_mes(mes)`: Devuelve la cantidad de películas estrenadas en un mes dado.
2. `cantidad_filmaciones_dia(dia)`: Devuelve la cantidad de películas estrenadas en un día específico.
3. `score_titulo(titulo_de_la_filmación)`: Devuelve título, año de estreno y score de popularidad de una película.
4. `votos_titulo(titulo_de_la_filmación)`: Devuelve cantidad de votos y promedio de puntuación de una película, si tiene al menos 2000 valoraciones.
5. `get_actor(nombre_actor)`: Devuelve el éxito del actor mediante el retorno total, cantidad de películas y promedio de retorno por película.
6. `get_director(nombre_director)`: Devuelve éxito del director, mostrando retorno, fecha de lanzamiento y ganancias de cada película.

### Sistema de Recomendación
El sistema de recomendación utiliza técnicas de similitud para sugerir cinco películas similares a la ingresada por el usuario, ordenadas por score de similaridad. Esta funcionalidad está disponible en el endpoint:

- `recomendacion(titulo)`: Devuelve una lista de cinco películas recomendadas, en orden descendente de similitud.

### Análisis Exploratorio de Datos (EDA)
El análisis exploratorio incluyó la identificación de outliers, análisis de correlaciones y visualizaciones como nubes de palabras para comprender mejor la distribución de títulos y patrones en los datos. Este análisis proporciona una base sólida para el modelo de recomendación.

## Despliegue
El proyecto se ha desplegado en **Render**. La API es accesible en línea y su funcionalidad se demostró en un video de 7 minutos que resume las consultas y el modelo de recomendaciones.

### Video Demostrativo
Un video muestra el funcionamiento de la API, consultas implementadas y una breve explicación del sistema de recomendación. Puedes acceder al video a través de este (https://drive.google.com/drive/folders/1_LrR5ch_1wxRHvjWumlr22B2e45-PJaL?usp=sharing).

## Criterios de Evaluación
1. **Código**: Prolijo, organizado y comentado. Uso adecuado de funciones y clases.
2. **Repositorio**: Archivos organizados y un README detallado para facilitar la comprensión del proyecto.
3. **MVP Completo**: Cumple con las transformaciones y requerimientos descritos, con un sistema de recomendación funcional.

## Datos Utilizados
- `movies_dataset.parquet`
- `credits.parquet`

El proyecto incluye un diccionario de datos para facilitar la comprensión de las columnas.

---

¡Gracias por revisar **Proyecto_CineSugerencias**! Espero que el sistema de recomendaciones sea útil y eficiente.
