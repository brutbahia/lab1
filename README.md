# Sistema de recomendación de películas

## Descripción del proyecto

Este es un MVP (Minimum Viable Product) de un sistema de recomendación de películas basado en un modelo de Machine Learning. El objetivo de este proyecto es solucionar un problema de negocio al ayudar a los usuarios a descubrir nuevas películas que les puedan gustar.

## Enfoque

El enfoque de este proyecto es desarrollar un modelo de Machine Learning capaz de recomendar 5 películas a partir del título de una película dada por el usuario. 

El modelo fue entrenado utilizando técnicas de aprendizaje automático y se utilizó el framework FastAPI para exponer el modelo como una API web. Además, se utilizó el servicio Render para realizar el deployment del modelo en la nube y hacerlo accesible a cualquier usuario que desee utilizarlo.

## Objetivos

Los objetivos principales de este proyecto son:

- Cumplir con los requisitos de ETL realizados en Jupyter Notebook. Puedes encontrar el archivo `etl.ipynb` [aquí](https://github.com/brutbahia/lab1/blob/master/etl.ipynb)
- Crear los endpoints que consumira la api. Puedes encontrar el archivo `main.py` [aquí](https://github.com/brutbahia/lab1/blob/master/main.py)
- Desarrollar un sistema de recomendación de películas basado en Machine Learning que sea capaz de recomendar 5 películas a partir del título de una película dada por el usuario,y agregarlo al archivo `main.py`  [aquí](https://github.com/brutbahia/lab1/blob/master/main.py)
- Utilizar el framework FastAPI para exponer el modelo como una API web y hacerlo accesible a cualquier usuario que desee utilizarlo
- Realizar un análisis exploratorio de los datos y buscar patrones interesantes que puedan ser utilizados en análisis posteriores. Puedes encontrar el archivo `EDA pruebas.ipynb` [aquí](https://github.com/brutbahia/lab1/blob/master/EDA%20pruebas.ipynb)
- Hacer que la data sea consumible por los departamentos de Analytics y Machine Learning para que puedan utilizarla en sus propios análisis, se utilizo la plataforma render para hacer el deployment y se alojo en "https://laboratorio-1-peliculas.onrender.com" [aquí](https://laboratorio-1-peliculas.onrender.com)

## Explicacion de archivos trabajados

- La carpeta `fastapi-env` es el entonrno virtual creado para ejecutar el modelo `main.py` en FastAPI.
- `Data_ML.csv` es la reduccion de los datos a solo las columnas utilizadas para el modelo de Machine Learning, ademas de cambiar name_Genres a variables categoricas codificadas de forma binaria.
- `EDA pruebas.ipynb` es en donde se realizo el análisis exploratorio de los datos.
- `ML.ipynb` es en donde se realizo las pruebas del modelo de Machine Larning asi como una calificacion del modelo utilizando la distancia euclidea
- `ejemplo de anidado.ipynb` se realizaron pruebas para el etl para desanidar las columnas anidadas
- `etl.ipynb`  es donde se realizo las transformacion de los datos
- `main.py` aqui es donde se encuentran los endpoints que consumira la api
- `movies_data.csv` es el archivo del data set original
- `movies_data_modificado.csv` es el archivo del data set modificado luego de pasar por la transformacion de los datos`etl.ipynb`
- `movies_data_modificado.pickle` es el archivo del data set modificado luego de pasar por la transformacion de los datos`etl.ipynb`, en formato pickle para mantener algunas caracteristicas del dataframe
-  `pruebas para main.ipynb` es el archivo donde se probo las funciones de los endpoints

##Contacto 
- Me pueden contactar para cualquier duda a travez de mi correo personal rieszepa@gmail.com
