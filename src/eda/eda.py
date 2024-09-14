# src/eda/eda.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

if not os.path.exists('images'):
    os.makedirs('images')

def plot_games_per_year(games_per_year, filename = 'game_launch_per_year.png'):
    sns.set(style='whitegrid')
    plt.figure(figsize=(14, 6))
    bars = sns.barplot(x=games_per_year['year_of_release'], y=games_per_year['games_count'].values, color='skyblue')
    plt.xlabel('Año de Lanzamiento')
    plt.ylabel('Cantidad de Juegos')
    plt.title('Juegos lanzados por año')
    bars.set_xticklabels(bars.get_xticklabels(), rotation=65, horizontalalignment='right')
    plt.savefig('images/' + filename)  # Guardar gráfica como imagen
    plt.close()  # Cerrar la figura para evitar que se mantenga en memoria

def plot_sales_by_platform(df, filename = 'sales_by_platform.png'):
    total_sales_by_platform = df.groupby('platform')['total_sales'].sum().sort_values(ascending=False)
    plt.figure(figsize=(12, 6))
    total_sales_by_platform.head(10).plot(kind='bar', color='skyblue')
    plt.title('Top 10 Plataformas con Mayores Ventas Totales')
    plt.xlabel('Plataforma')
    plt.ylabel('Ventas Totales (en millones)')
    plt.xticks(rotation=45)
    plt.savefig('images/' + filename)  # Guardar gráfica como imagen
    plt.close()  # Cerrar la figura para evitar que se mantenga en memoria

def plot_sales_distribution_per_year(df, filename='sales_per_year.png'):
    # Seleccionar plataformas para análisis detallado
    selected_platforms = ['PS2', 'X360', 'PS3']
    platform_sales_over_time = df[df['platform'].isin(selected_platforms)]
    platform_sales_annual = platform_sales_over_time.pivot_table(index='year_of_release', columns='platform', values='total_sales', aggfunc='sum')
    plt.figure(figsize=(14, 8))
    for platform in selected_platforms:
        plt.plot(platform_sales_annual.index, platform_sales_annual[platform], marker='o', label=platform)

    plt.title('Ventas Anuales por Plataforma')
    plt.xlabel('Año')
    plt.ylabel('Ventas Totales (en millones)')
    plt.legend(title='Plataforma')
    plt.grid(True)
    plt.savefig('images/' + filename)  # Guardar gráfica como imagen
    plt.close()  # Cerrar la figura para evitar que se mantenga en memoria

def plot_sales_since_2010(df, filename='sales_since_2010.png'):
    # Filtrar los datos para incluir solo los años desde 2010 en adelante
    data_since_2010 = df[df['year_of_release'] >= 2010]
    # Calcular ventas totales por plataforma en este período
    total_sales_by_platform_since_2010 = data_since_2010.groupby('platform')['total_sales'].sum().sort_values(ascending=False)
    plt.figure(figsize=(12, 6))
    total_sales_by_platform_since_2010.plot(kind='bar', color='skyblue')
    plt.title('Ventas Totales por Plataforma desde 2010')
    plt.xlabel('Plataforma')
    plt.ylabel('Ventas Totales (en millones)')
    plt.xticks(rotation=45)
    plt.savefig('images/' + filename)  # Guardar gráfica como imagen
    plt.close()  # Cerrar la figura para evitar que se mantenga en memoria

def plot_tendences_platform(df, filename='tendences_per_platform.png'):
    # Seleccionar plataformas para análisis de tendencias
    platforms_for_trend_analysis = ['PS4', 'XOne', '3DS']
    data_since_2010 = df[df['year_of_release'] >= 2010]
    # Filtrar datos para incluir solo las plataformas seleccionadas
    trend_data = data_since_2010[data_since_2010['platform'].isin(platforms_for_trend_analysis)]

    # Agrupar por plataforma y año de lanzamiento, y sumar las ventas totales
    annual_sales_trends = trend_data.pivot_table(index='year_of_release', columns='platform', values='total_sales', aggfunc='sum')

    # Crear gráficos de líneas para las tendencias anuales de ventas
    plt.figure(figsize=(12, 7))
    for platform in platforms_for_trend_analysis:
        plt.plot(annual_sales_trends.index, annual_sales_trends[platform], marker='o', label=platform)

    plt.title('Tendencias Anuales de Ventas por Plataforma desde 2010')
    plt.xlabel('Año')
    plt.ylabel('Ventas Totales (en millones)')
    plt.legend(title='Plataforma')
    plt.grid(True)
    plt.savefig('images/' + filename)  # Guardar gráfica como imagen
    plt.close()  # Cerrar la figura para evitar que se mantenga en memoria

def plot_relevant_platform(df, filename='relevant_platforms.png'):
    # Filtrar los datos para incluir solo los años desde 2010 en adelante
    data_since_2010 = df[df['year_of_release'] >= 2010]
    # Calcular ventas totales por plataforma en este período
    total_sales_by_platform_since_2010 = data_since_2010.groupby('platform')['total_sales'].sum().sort_values(ascending=False)
    # Filtrar datos para incluir las plataformas más relevantes identificadas anteriormente
    relevant_platforms = total_sales_by_platform_since_2010.index[:10]  # Seleccionar las 10 plataformas principales desde 2010
    sales_data_for_boxplot = data_since_2010[data_since_2010['platform'].isin(relevant_platforms)]
    # Crear un diagrama de caja para las ventas globales de juegos por plataforma
    plt.figure(figsize=(14, 8))
    sns.boxplot(x='platform', y='total_sales', data=sales_data_for_boxplot, palette='coolwarm', log_scale=10)
    # Define las marcas y etiquetas para una escala logarítmica base 10
    yticks = [10**i for i in range(-2, 3)]  # Genera una lista [0.01, 0.1, 1, 10, 100]
    yticklabels = ['0.01M', '0.1M', '1M', '10M', '100M']

    plt.yticks(ticks=yticks, labels=yticklabels)  # Establecer las marcas y etiquetas personalizadas

    plt.title('Distribución de Ventas Globales de Juegos por Plataforma desde 2010')
    plt.xlabel('Plataforma')
    plt.ylabel('Ventas Globales (en millones)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig('images/' + filename)  # Guardar gráfica como imagen
    plt.close()  # Cerrar la figura para evitar que se mantenga en memoria
    
def plot_critic_review(df, filename='reviews_critics_and_users.png'):
    # Filtrar los datos para incluir solo los años desde 2010 en adelante
    data_since_2010 = df[df['year_of_release'] >= 2010]
    # Calcular ventas totales por plataforma en este período
    total_sales_by_platform_since_2010 = data_since_2010.groupby('platform')['total_sales'].sum().sort_values(ascending=False)
    # Filtrar datos para incluir las plataformas más relevantes identificadas anteriormente
    relevant_platforms = total_sales_by_platform_since_2010.index[:10]  # Seleccionar las 10 plataformas principales desde 2010
    sales_data_for_boxplot = data_since_2010[data_since_2010['platform'].isin(relevant_platforms)]
    # Suponiendo que 'sales_data_for_boxplot' es tu DataFrame y ya está cargado con los datos adecuados
    # Crear una copia explícita del DataFrame para evitar SettingWithCopyWarning
    platform_data = sales_data_for_boxplot[sales_data_for_boxplot['platform'] == 'PS4'].copy()
    platform_data['critic_score'] = pd.to_numeric(platform_data['critic_score'], errors='coerce')
    platform_data['user_score'] = pd.to_numeric(platform_data['user_score'], errors='coerce')


    # Eliminar valores NaN para el análisis de correlación
    platform_data = platform_data.dropna(subset=['critic_score', 'user_score', 'total_sales'])

    # Crear gráficos de dispersión
    plt.figure(figsize=(14, 6))

    # Gráfico de dispersión para las reseñas de críticos vs. ventas
    plt.subplot(1, 2, 1)
    sns.scatterplot(x='critic_score', y='total_sales', data=platform_data)
    plt.title('Críticas de Profesionales vs. Ventas en PS4')
    plt.xlabel('Puntuación de Críticos')
    plt.ylabel('Ventas Globales (en millones)')

    # Gráfico de dispersión para las reseñas de usuarios vs. ventas
    plt.subplot(1, 2, 2)
    sns.scatterplot(x='user_score', y='total_sales', data=platform_data)
    plt.title('Reseñas de Usuarios vs. Ventas en PS4')
    plt.xlabel('Puntuación de Usuarios')
    plt.ylabel('Ventas Globales (en millones)')

    plt.tight_layout()
    plt.savefig('images/' + filename)  # Guardar gráfica como imagen
    plt.close()  # Cerrar la figura para evitar que se mantenga en memoria

def plot_multiplatform_games(df, filename='multiplatform_games_sales.png'):
    data_since_2010 = df[df['year_of_release'] >= 2010]
    # Filtrar juegos que están disponibles en múltiples plataformas
    multiplatform_games = data_since_2010.groupby('name').filter(lambda x: len(x['platform'].unique()) > 1)

    # Crear una tabla pivot para comparar las ventas en diferentes plataformas por juego
    platform_sales = multiplatform_games.pivot_table(index='name', columns='platform', values='total_sales')

    # Para simplificar, seleccionamos solo dos plataformas para la comparación, por ejemplo, PS4 y XOne
    platform_sales_subset = platform_sales[['PS4', 'XOne']].dropna()
    columns_to_plot = ['PS4', 'XOne']

    # Ordenamos los juegos con mayores ventas en ambas plataformas creando una columna que muestre el total 
    platform_sales_subset['total_platform_sale'] = platform_sales_subset.sum(axis=1) 
    platform_sales_subset = platform_sales_subset.sort_values('total_platform_sale', ascending=False)

    # Seleccionamos solo el top 5 de mayores ventas
    platform_sales_subset = platform_sales_subset.head(5)

    # Graficar las ventas de los juegos en PS4 vs XOne como gráfico de barras
    platform_sales_subset[columns_to_plot].plot(kind='bar', figsize=(14, 8))
    plt.title('Comparación de Ventas de Juegos Multiplataforma en PS4 vs XOne')
    plt.xlabel('Nombre del Juego')
    plt.xticks(rotation = 360)
    plt.ylabel('Ventas Globales (en millones)')
    plt.savefig('images/' + filename)  # Guardar gráfica como imagen
    plt.close()  # Cerrar la figura para evitar que se mantenga en memoria

def plot_games_per_genre(df, filename='games_per_genre.png'):
    data_since_2010 = df[df['year_of_release'] >= 2010]
    # Agrupamos los datos por genero, Calculamos promedios de  las ventas totales para cada genero
    genre_average_sales = data_since_2010.groupby('genre')['total_sales'].mean().sort_values(ascending=False)

    # Crea un gráfico de barras para las ventas promedio por género
    plt.figure(figsize=(14, 7))
    genre_average_sales.plot(kind='bar', color='coral')
    plt.title('Ventas Promedio por Juego en cada Género')
    plt.xlabel('Género')
    plt.ylabel('Ventas Promedio por Juego (en millones)')
    plt.xticks(rotation=45)
    plt.savefig('images/' + filename)  # Guardar gráfica como imagen
    plt.close()  # Cerrar la figura para evitar que se mantenga en memoria
    
def get_top_genres_by_region(df):
    # Agrupar las ventas por género y región
    genre_sales_by_region = df.groupby('genre').agg({
        'na_sales': 'sum',
        'eu_sales': 'sum',
        'jp_sales': 'sum'
    })

    # Obtener las 5 principales géneros por región
    top_genre_na = genre_sales_by_region['na_sales'].sort_values(ascending=False).head(5)
    top_genre_eu = genre_sales_by_region['eu_sales'].sort_values(ascending=False).head(5)
    top_genre_jp = genre_sales_by_region['jp_sales'].sort_values(ascending=False).head(5)

    # Retornar los resultados en un diccionario para usarlos en el reporte final
    return {
        'top_genre_na': top_genre_na,
        'top_genre_eu': top_genre_eu,
        'top_genre_jp': top_genre_jp
    }

def get_top_platforms_by_region(df):
    # Las cinco plataformas principales por región
    platform_sales_by_region = df.groupby('platform').agg({
        'na_sales': 'sum',
        'eu_sales': 'sum',
        'jp_sales': 'sum'
    })

    top_platforms_na = platform_sales_by_region['na_sales'].sort_values(ascending=False).head(5)
    top_platforms_eu = platform_sales_by_region['eu_sales'].sort_values(ascending=False).head(5)
    top_platforms_jp = platform_sales_by_region['jp_sales'].sort_values(ascending=False).head(5)

    # Retornar los resultados en un diccionario para usarlos en el reporte final
    return {
        'top_platforms_na': top_platforms_na,
        'top_platforms_eu': top_platforms_eu,
        'top_platforms_jp': top_platforms_jp
    }