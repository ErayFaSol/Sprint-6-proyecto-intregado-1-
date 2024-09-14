# src/main.py
from preprocessing.preprocessing import preprocess_data
from analysis.eda import plot_games_per_year
from utilities.helpers import load_data
import params

# Cargar datos
df = load_data(params.DATA_PATH)

# Preprocesar datos
df_cleaned = preprocess_data(df)

# Análisis Exploratorio
plot_games_per_year(df_cleaned)

# Modelos (si ya tienes esta parte)
# from models.predict_model import train_model
# model, X_test, y_test = train_model(df_cleaned)
