# src/analysis/eda.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_games_per_year(games_per_year):
    sns.set(style='whitegrid')
    plt.figure(figsize=(14, 6))
    bars = sns.barplot(x=games_per_year['year_of_release'], y=games_per_year['games_count'].values, color='skyblue')
    plt.xlabel('Año de Lanzamiento')
    plt.ylabel('Cantidad de Juegos')
    plt.title('Juegos lanzados por año')
    bars.set_xticklabels(bars.get_xticklabels(), rotation=65, horizontalalignment='right')
    plt.show()
