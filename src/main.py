from preprocessing.preprocessing import load_data
from eda.eda import *
from hypothesis_testing.hypothesis_test import platform_hypothesis, genre_hypothesis
from utils.generate_report import save_report

# Cargar y preprocesar datos
df = load_data("datasets/games.csv")
games_per_year = df.groupby('year_of_release').size().reset_index(name='games_count')
data_since_2010 = df[df['year_of_release'] >= 2010]
# Análisis exploratorio
plot_games_per_year(games_per_year)
plot_sales_by_platform(df)
plot_sales_distribution_per_year(df)
plot_sales_since_2010(df)
plot_tendences_platform(df)
plot_relevant_platform(df)
plot_critic_review(df)
plot_multiplatform_games(df)
plot_games_per_genre(df)

# Obtener los géneros principales por región
top_genres_by_region = get_top_genres_by_region(data_since_2010)

top_platforms_by_region = get_top_platforms_by_region(data_since_2010)

# Top generos por region
print("Top géneros en Norteamérica:")
print(top_genres_by_region['top_genre_na'])

print("\nTop géneros en Europa:")
print(top_genres_by_region['top_genre_eu'])

print("\nTop géneros en Japón:")
print(top_genres_by_region['top_genre_jp'])

# top plataforma por region
print("Top plataforma en Norteamérica:")
print(top_platforms_by_region['top_platforms_na'])

print("\nTop plataforma en Europa:")
print(top_platforms_by_region['top_platforms_eu'])

print("\nTop plataforma en Japón:")
print(top_platforms_by_region['top_platforms_jp'])



# Pruebas de hipótesis
# hipotesis plataforma
xbox_scores = data_since_2010[(data_since_2010['platform'] == 'XOne') & (data_since_2010['user_score'].notna())]['user_score']
pc_scores = data_since_2010[(data_since_2010['platform'] == 'PC') & (data_since_2010['user_score'].notna())]['user_score']

pvalue_hypothesis_1 = platform_hypothesis(xbox_scores, pc_scores)
# Hipotesis genero
action_scores = data_since_2010[(data_since_2010['genre'] == 'Action') & (data_since_2010['user_score'].notna())]['user_score']
sports_scores = data_since_2010[(data_since_2010['genre'] == 'Sports') & (data_since_2010['user_score'].notna())]['user_score']
pvalue_hypothesis_2 = genre_hypothesis(action_scores, sports_scores)

report_content = """
<h1>Análisis de Ventas de Videojuegos</h1>

<h2>Top 5 Géneros por Región</h2>
<h3>Top géneros en Norteamérica:</h3>
{na_genres}
<h3>Top géneros en Europa:</h3>
{eu_genres}
<h3>Top géneros en Japón:</h3>
{jp_genres}

<h2>Top 5 Plataformas por Región</h2>
<h3>Top plataformas en Norteamérica:</h3>
{na_platforms}
<h3>Top plataformas en Europa:</h3>
{eu_platforms}
<h3>Top plataformas en Japón:</h3>
{jp_platforms}

<h2>Gráficas</h2>
<img src="images/game_launch_per_year.png" alt="Juegos lanzados por año">
<img src="images/sales_by_platform.png" alt="Ventas por plataforma">
<img src="images/sales_per_year.png" alt="Ventas anuales por plataforma">
<img src="images/sales_since_2010.png" alt="Ventas desde 2010">
<img src="images/tendences_per_platform.png" alt="Tendencias de ventas por plataforma">
<img src="images/relevant_platforms.png" alt="Distribución de ventas por plataforma">
<img src="images/reviews_critics_and_users.png" alt="Críticas vs Ventas en PS4">
<img src="images/multiplatform_games_sales.png" alt="Comparación de ventas multiplataforma">
<img src="images/games_per_genre.png" alt="Ventas por género">

<h2>Resultados de las Pruebas de Hipótesis</h2>
<p><b>Hipótesis 1:</b> Las calificaciones promedio de los usuarios para las plataformas Xbox One y PC son las mismas.</p>
<p>Resultado de la prueba: p-value = {pvalue_hypothesis_1}</p>

<p><b>Hipótesis 2:</b> Las calificaciones promedio de los usuarios para los géneros de Acción y Deportes son diferentes.</p>
<p>Resultado de la prueba: p-value = {pvalue_hypothesis_2}</p>
"""

# Formatear el contenido del reporte con los resultados
report_content = report_content.format(
    na_genres=top_genres_by_region['top_genre_na'].to_frame().to_html(),
    eu_genres=top_genres_by_region['top_genre_eu'].to_frame().to_html(),
    jp_genres=top_genres_by_region['top_genre_jp'].to_frame().to_html(),
    na_platforms=top_platforms_by_region['top_platforms_na'].to_frame().to_html(),
    eu_platforms=top_platforms_by_region['top_platforms_eu'].to_frame().to_html(),
    jp_platforms=top_platforms_by_region['top_platforms_jp'].to_frame().to_html(),
    pvalue_hypothesis_1=pvalue_hypothesis_1,
    pvalue_hypothesis_2=pvalue_hypothesis_2
)

# Guardar el reporte final en HTML
save_report(report_content, "reporte_final.html")