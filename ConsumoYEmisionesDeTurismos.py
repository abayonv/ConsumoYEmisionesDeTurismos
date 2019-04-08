#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
import json
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import argparse

#página inicial
url0 = "http://coches.idae.es/base-datos/marca-y-modelo"

#página que realiza la búsqueda
url = "http://coches.idae.es/ajax"

#creación de variables
headerValues={}
payload={}
payloadDetalle={}

# Rellenar la cabecera con los valores necesarios
headerValues["Accept"] = "application/json, text/javascript, */*; q=0.01"
headerValues["Connection"] = "keep-alive"
headerValues["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
headerValues["Host"] =  "coches.idae.es"
headerValues["Origin"] = "http://coches.idae.es"
headerValues["Referer"] = "http://coches.idae.es/base-datos/marca-y-modelo"
headerValues["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"

# Crear una sesión
s = requests.session()

# Abrir la página inicial
r1 = s.get(url0)

#Recoger la respuesta de esa página
soup = bs(r1.text,'lxml')

#buscar el cotenido del elemento _token
csrf_token = soup.select_one('meta[name="_token"]')['content']

#Asignar el valor localizado al elemento toquen de headers 
headerValues['X-CSRF-Token'] = csrf_token
headerValues["X-Requested-With"] = "XMLHttpRequest"

#Recoger también los cookies de la página de busqueda
cookie = r1.cookies

# Seleccionamos el contenido correspondiente a las diferentes marcas (donde cada marca se identifica con un "value")
select_marca= soup.find(id="marca")

# Generamos un listado con el nombre de todas las marcas
# Este listado lo utilizaremos como ayuda, para saber todas las marcas que hay cuanda haya que filtrar por una de ellas.
listado_marcas=[]
for i in select_marca.find_all('option'):
    listado_marcas.append(i.string)
       
# Para introducir la marca de coche al ejecutar el script
seguimos = True
while seguimos == True:
    print('Escribe el nombre de uno de los siguientes coches:{}'.format(listado_marcas))
    marca_seleccionada = input ("Seleccion: ")
    seguimos = False

# Obtenemos el campo "value" de la marca que se ha seleccionado
for i in select_marca.find_all('option'):
    if (i.string==marca_seleccionada):
        codigo_marca=(i['value'])
        

#Rellenar el payload
payload["draw"] = "1"
payload["columns[0][data]"] = "0"
payload["columns[0][name]"] = ""
payload["columns[0][searchable]"] = "true"
payload["columns[0][orderable]"] = "true"
payload["columns[0][search][value]"] = "" 
payload["columns[0][search][regex]"] = "false"
payload["columns[1][data]"] = "1"
payload["columns[1][name]"] = ""
payload["columns[1][searchable]"] = "true"
payload["columns[1][orderable]"] = "false"
payload["columns[1][search][value]"] =  ""
payload["columns[1][search][regex]"] = "false"
payload["columns[2][data]"] = "2"
payload["columns[2][name]"] = ""
payload["columns[2][searchable]"] = "true"
payload["columns[2][orderable]"] = "true"
payload["columns[2][search][value]"] = "" 
payload["columns[2][search][regex]"] = "false"
payload["columns[3][data]"] = "3"
payload["columns[3][name]"] = ""
payload["columns[3][searchable]"] = "true"
payload["columns[3][orderable]"] = "true"
payload["columns[3][search][value]"] =  ""
payload["columns[3][search][regex]"] = "false"
payload["columns[4][data]"] = "4"
payload["columns[4][name]"] = ""
payload["columns[4][searchable]"] = "true"
payload["columns[4][orderable]"] = "true"
payload["columns[4][search][value]"] = ""
payload["columns[4][search][regex]"] = "false"
payload["columns[5][data]"] = "5"
payload["columns[5][name]"] = ""
payload["columns[5][searchable]"] = "true"
payload["columns[5][orderable]"] = "true"
payload["columns[5][search][value]"] = "" 
payload["columns[5][search][regex]"] = "false"
payload["order[0][column]"] = "0"
payload["order[0][dir]"] = "asc"
payload["start"] = "0"
payload["length"] = ""
payload["search[value]"] = ""
payload["search[regex]"] = "false"
payload["_token"] = csrf_token
payload["campo"] = "listado"
payload["ciclo"] = "wltp"

# conjunto de filtros que se utiliza en la llamada
payload["filtros"] = "_token="+csrf_token+"&tipo=marca-y-modelo&motorizacion=&categoria=&segmento=&marca="+codigo_marca+"&modelo=&datos_nedc_length=&datos_wltp_length="

#Se realiza la llamada con la url que realiza la busqueda, las cookies, la cabecera y el payload
r2 = s.post(url, cookies=cookie, data= payload, headers = headerValues,verify=True)

#Imprimir el resultado de la llamada
#print("codigo estado",r2.status_code)

# Cargar la salida en una variable d formato json
json_salida = json.loads(r2.text)

# Recoger el contenido del elemento data
json_data = json_salida["data"]


# Creamos un dataframe vacio, con el nombre de las cabeceras 
df_coches = pd.DataFrame(columns = ["Modelo","Clasificación energética ","Consumo mínimo (l/100Km)","Consumo máximo (l/100Km)","Emisiones mínimas (gCO2/km)","Emisiones máximas (gCO2/km)"])

# Recorremos la lista "json_data" para obtener los datos que nos interesan
for i in range(len(json_data)):
    modelo=json_data[i][0]
    clasificacion=json_data[i][1] # Más abajo editaremos esta cadena de texto para quedarnos solo con lo que nos interesa
    consumo_min=json_data[i][2]
    consumo_max=json_data[i][3]
    emisiones_min=json_data[i][4]
    emisiones_max=json_data[i][5]
    
    
    # Dividimos la cadena de texto por donde hay ":", de manera que obtenemos 3 subcadenas
    # De las 3 subcadenas nos quedamos con la última: [2] que contiene el texto de la clasificación(' G">')
    clasificacion=clasificacion.split(':')[2]

    # Como queremos solo el texto sin signos, no queremos ni el espacio inicial ni los dos signos del final "> 
    # indicamos que del string solo nos coja de la posición 1 a la -2
    clasificacion=clasificacion[1:-2]

    # Añadimos los datos de cada modelo de coche obtenido a nuestro dataframe
    df_coches.loc[len(df_coches)]=[modelo,clasificacion,consumo_min,consumo_max,emisiones_min,emisiones_max]

# Mostramos por pantalla el dataframe    
print(df_coches)

# Crea el archivo de datos en formato .csv
df_coches.to_csv('data_coches.csv')

###################### fin codigo añadido #################################################################


# In[ ]:




