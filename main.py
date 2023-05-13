#importamos las librerias
from fastapi import FastAPI

app = FastAPI()
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances

# Lee el archivo CSV en un DataFrame de Pandas
df = pd.read_csv('movies_dataset_modificado.csv', low_memory=False)


# http://127.0.0.1:8000

@app.get("/")
def indes():
    return "holamundo"

@app.get("/Mes/{mes}")
def peliculas_mes(mes:str):
            
    # seleccionar las filas que corresponden al mes dado
    df_mes = df[df['release_month'] == mes]
    
    # contar la cantidad de filas
    respuesta = len(df_mes)
    
    # retornar la cantidad
    return {'mes':mes, 'cantidad':respuesta}
    

@app.get("/Dia/{dia}")
def peliculas_dia(dia:str):
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



df["name_Genres"] = df["name_Genres"].apply(lambda x: x.replace("[", "").replace("]", "").replace("'", "").replace(", ", ","))

data = df[['title', 'vote_average', 'name_Genres', "release_year", "name_production_companies","overview"]]

similarity_matrix = pairwise_distances(data.pivot_table(index='name_Genres', columns='release_year', values='vote_average', fill_value=0), metric='cosine')


@app.get("/Recomendacion/{titulo}")
def recomendacion(titulo:str):
    # Buscar la película seleccionada por el usuario en el DataFrame
    idx = data[data['title'] == titulo].index[0]
    
    # Ordenar la matriz de similaridad para obtener las películas más similares
    similar_movie_indices = np.argsort(similarity_matrix[idx])
    
    # Seleccionar las primeras 5 películas más similares y obtener sus títulos
    recommended_movies = []
    for i in similar_movie_indices:
        if data.iloc[i]['title'] != titulo:
            recommended_movies.append(data.iloc[i]['title'])
        if len(recommended_movies) == 5:
            break
    
    # Devolver una lista con los títulos de las películas recomendadas
    return {'lista recomendada': recommended_movies}



