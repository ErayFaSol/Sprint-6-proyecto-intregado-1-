# Sprint 6 - Proyecto Integrado 1

## Descripción del Proyecto
Este proyecto tiene como objetivo analizar datos de ventas de videojuegos, reseñas de usuarios y expertos, y otros factores (géneros, plataformas, etc.) para identificar patrones que determinen el éxito de un juego. La empresa Ice, que vende videojuegos a nivel global, utilizará este análisis para detectar proyectos prometedores y planificar campañas publicitarias efectivas.

Los datos disponibles cubren el período hasta 2016, y se utilizarán para planificar las campañas de marketing para 2017. Este ejercicio proporciona experiencia práctica en el trabajo con datos históricos y la identificación de tendencias clave en la industria de los videojuegos.

## Dataset
El dataset contiene las siguientes columnas:

Name: Nombre del videojuego
Platform: Plataforma (Xbox, PlayStation, etc.)
Year_of_Release: Año de lanzamiento
Genre: Género del videojuego
NA_sales: Ventas en Norteamérica (en millones de USD)
EU_sales: Ventas en Europa (en millones de USD)
JP_sales: Ventas en Japón (en millones de USD)
Other_sales: Ventas en otras regiones (en millones de USD)
Critic_Score: Puntuación de los críticos (máximo de 100)
User_Score: Puntuación de los usuarios (máximo de 10)
ESRB_Rating: Clasificación de edad de ESRB (Adolescente, Adulto, etc.)
Objetivo
El objetivo principal es identificar los factores que contribuyen al éxito de un videojuego en términos de ventas globales, tomando en cuenta factores como la plataforma, género, puntuaciones de usuarios y críticos, y región geográfica.

Pasos del Proyecto
Carga y Exploración de Datos

Cargar los datos desde /datasets/games.csv.
Explorar la información general del dataset.
Preprocesamiento de Datos

Limpiar los datos y tratar los valores ausentes.
Convertir los tipos de datos según sea necesario.
Crear nuevas columnas, como las ventas totales globales.
Análisis Exploratorio de Datos (EDA)

Analizar el número de lanzamientos de juegos por año.
Evaluar las ventas por plataforma y género.
Investigar cómo las reseñas afectan las ventas.
Comparar las ventas por región (NA, UE, JP).
Pruebas de Hipótesis

Comparar las calificaciones promedio entre plataformas como Xbox y PC.
Comparar las calificaciones entre géneros, como Acción y Deportes.
Conclusiones

Basado en el análisis, formular conclusiones sobre qué factores predicen el éxito de un videojuego.
Instrucciones de Instalación
Para ejecutar este proyecto en tu entorno local:

Clona el repositorio:

bash
Copiar código
git clone https://github.com/ErayFaSol/Sprint-6-proyecto-intregado-1-.git
cd Sprint-6-proyecto-intregado-1-
Instala las dependencias necesarias:

bash
Copiar código
pip install -r requirements.txt
Ejecuta el notebook en Jupyter:

bash
Copiar código
jupyter notebook proyecto6.ipynb
Visualizaciones
Este proyecto incluye varias visualizaciones para analizar los datos, como:

Diagramas de dispersión para evaluar la correlación entre las puntuaciones y las ventas.
Diagramas de caja para comparar las ventas entre diferentes plataformas.
Gráficos de barras para mostrar las ventas por región.