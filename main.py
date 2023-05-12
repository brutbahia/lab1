#importamos las librerias
from fastapi import FastAPI

app = FastAPI()
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances

# Lee el archivo CSV en un DataFrame de Pandas
df = pd.read_csv('E:\hENRYDATASEMANAS\lab1\movies_dataset_modificado.csv', low_memory=False)


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

df2 = df[["title","name_Genres", "name_Genres_str",'vote_average']]
df2 = df2.dropna(subset=['name_Genres'])
df2 = df2.dropna(subset=['name_Genres_str'])
df2 = df2.dropna(subset=['title'])
df2['title'] = df2['title'].astype(str)

@app.get("/Recomendacion/{titulo}")
def get_movie_recommendations(titulo:str):

    df1 = df2.sample(n=10000)
    # Obtenga el índice de la película en la similarity matrix 
    
    movie_similarity = 1 - pairwise_distances(df1.pivot_table(index='title',columns='name_Genres', values='vote_average').fillna(0), metric='cosine')
    movie_index = df2[df2['title'] == titulo].index[0]

    # Get the similarity scores for all movies compared to the given movie
    similarity_scores = movie_similarity[movie_index]

    # Sort the scores from highest to lowest
    similar_movie_indices = np.argsort(-similarity_scores)

    # Obtén las mejores películas más similares
    top_movie_indices = similar_movie_indices[1:6]

    # Obtén los títulos de las mejores películas más similares
    respuesta = [df2.iloc[index]['title'] for index in top_movie_indices]

    return {'lista recomendada': respuesta}



