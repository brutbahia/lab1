#importamos las librerias
from fastapi import FastAPI

app = FastAPI()
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances

# Lee el archivo CSV procesado en etl.ipynb en un DataFrame con Pandas 
df = pd.read_csv('movies_dataset_modificado.csv', low_memory=False)


# http://127.0.0.1:8000

@app.get("/")
def indes():
    return "holamundo"

@app.get("/Mes/{mes}")
def peliculas_mes(mes:str):
    meses_validos = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    if mes not in meses_validos:
        return 'Formato no válido o mes mal escrito. Por favor, introducir con la primera letra en mayúscula. Ejemplo: Marzo'       
    # seleccionar las filas que corresponden al mes dado

    df_mes = df[df['release_month'] == mes]
    
    # contar la cantidad de filas
    respuesta = len(df_mes)
    
    # retornar la cantidad
    return {'mes':mes, 'cantidad':respuesta}
    

@app.get("/Dia/{dia}")
def peliculas_dia(dia:str):
    dias_validos = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    if dia not in dias_validos:
        return 'Formato no válido o día mal escrito. Por favor, introducir con la primera letra en mayúscula. Ejemplo: Miércoles'

    # cargar el conjunto de datos
        
    # seleccionar las filas que corresponden al mes dado
    df_dia = df[df['release _day'] == dia]
    
    # contar la cantidad de filas
    respuesta = len(df_dia)
    
    # retornar la cantidad
    return {'dia':dia, 'cantidad':respuesta}



@app.get("/Franquicia/{franquicia}")
def franquicia(franquicia:str):
     
    # seleccionar las filas que corresponden a la franquicia dada
    df_franquicia = df[df['name_collection'] == franquicia]
        
    # contar la cantidad de películas
    cantidad = len(df_franquicia)
        
    # calcular la ganancia total y promedio
    ganancia_total = df_franquicia['revenue'].sum()
    ganancia_promedio = df_franquicia['revenue'].mean()
        
    # retornar un diccionario con los resultados
    return {'franquicia':franquicia, 'cantidad':cantidad, 'ganancia_total':ganancia_total, 'ganancia_promedio':ganancia_promedio}
    
    

@app.get("/Pais/{pais}")
def peliculas_pais(pais:str):
    df_pais = df[df['name_production_countries'].apply(lambda x: pais in x if pd.notna(x) else False)]
    
    # contar la cantidad de películas
    cantidad = len(df_pais)
    
    # retornar un diccionario con los resultados
    return {'pais':pais, 'cantidad':cantidad}


@app.get("/Productor/{productora}")
def productoras(productora:str):
   
    # seleccionar las filas que contienen la productora dada en la lista de productoras
    df_productora = df[df['name_production_companies'].apply(lambda x: productora in x if pd.notna(x) else False)]

    # calcular la ganancia total y la cantidad de películas producidas
    ganancia_total = df_productora['revenue'].sum()
    cantidad = len(df_productora)

    # retornar un diccionario con los resultados
    return {'productora':productora, 'ganancia_total':ganancia_total, 'cantidad':cantidad}

@app.get("/Pelicula/{pelicula}")
def retorno(pelicula:str):
    
    # seleccionar la fila correspondiente a la película dada
    df_pelicula = df[df['title'] == pelicula]
    
    # obtener los valores de inversión, ganancia , año de lanzamiento retorno
    inversion = df_pelicula['budget'].values[0]
    ganancia = df_pelicula['revenue'].values[0]
    anio = df_pelicula['release_year'].values[0]
    retorno = df_pelicula['return'].values[0]
    
    
    return {'pelicula': pelicula, 'inversion': inversion, 'ganacia': ganancia, 'retorno': retorno, 'anio': anio}

#Datos Preprocesados en ML.ipynb variables categoricas codificadas archivo pickle para mantener formato
data= pd.read_pickle('Data_ML.pickle')

from sklearn.model_selection import train_test_split

# Separar los datos en conjuntos de entrenamiento y prueba
train_data, test_data = train_test_split(data, test_size=0.25, random_state=42)

from sklearn.neighbors import NearestNeighbors

# Crear una matriz de similitud entre películas
model = NearestNeighbors(metric='hamming', algorithm='auto')
model.fit(train_data.drop(['title'], axis=1))

@app.get("/Recomendacion/{titulo}")
def get_recommendations( movie_title):
    # Obtener el índice de la película en el conjunto de datos
    idx = data[data['title'] == movie_title].index[0]
    # Obtener las películas más similares
    distances, indices = model.kneighbors(data.iloc[idx, 1:].values.reshape(1, -1), n_neighbors=6)
    # Obtener los títulos de las películas recomendadas
    recommended_movies = [data.iloc[indices[0][i+1]]['title'] for i in range(5)]

    return { 'lista recomendada':recommended_movies}







