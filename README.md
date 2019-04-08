# Descripcion
El conjunto de datos que se generado en este trabajo contiene detalles sobre el consumo de carburante y emisiones de CO2 de los turismos nuevos que se comercializan en España. Esta información se ha recogido de la página web http://coches.idae.es que forma parte programa del Instituto para la Diversificación y Ahorro de Energía (IDAE), organismo adscrito al Ministerio para la Transición Ecológica.* 

# Miembros del equipo
Los actividad ha sido realizada en grupo por los siguientes miembros:
* Elena Ruiz Martinez
* Alberto Bayón Valtierra

# Descripción de los ficheros
* **ConsumoYEmisionesDeTurismos.py**: script que ejecuta el proceso de scraping y retorna un fichero .csv con la información correspondiente a la marca de coche que se haya seleccionado.
* **ConsumoYEmisionesDeTurismos_marca_Jaguar.csv**: dataset resultante de haber seleccionado la marca de coche "Jaguar"
* **Respuestas_Practica1.pdf**: PDF con las respuestas planteadas en la práctica

El script se debe ejecutar de la siguiente manera:  
`python ConsumoYEmisionesDeTurismos.py`  
Al ejecutarlo nos aparecerá por pantalla el siguiente mensaje:    
`Escribe el nombre de uno de los siguientes coches:['* Cualquiera', 'Abarth', 'Aixam', 'Alfa Romeo', 'ALKE', 'ASKOLL', 'Aston Martin', 'Audi', 'Audi Canarias', 'BE ELECTRIC DRIVE', 'Bentley', 'BMW', 'BMW i', 'BYD', 'Cadillac', 'CAGB A4', 'Car-bus.net', 'Chevrolet', 'Citroën', 'Comarth', 'Corvette', 'Dacia', 'Daihatsu', 'Daimler', 'Daimler Autobuses', 'DFSK', 'DS', 'E-Fun', 'E-MAX', 'E-RIDER', 'ECCITY', 'Ecooter', 'Esagono Energia', 'Estrima', 'Ferrari', 'Fiat', 'Ford', 'Fuso', 'GEM', 'Going Green', 'GOODYEAR', 'Goupil', 'Govecs', 'Honda', 'Hummer', 'Hyundai', 'Hyundai Canarias', 'Infiniti', 'Irizar', 'Isuzu', 'Iveco', 'Jaguar', 'Jeep', 'JIAYUAN', 'Kia', 'Kia Canarias', 'KING LONG', 'LADA', 'Lada-Vaz', 'Lancia', 'Land Rover', 'Lexus', 'Lexus Canarias', 'LIGIER', 'LIGIER PROFESSIONAL', 'LITTLE', 'Lotus', 'Mahindra', 'MAN', 'MARSHELL', 'Maserati', 'MAXUS', 'Mazda', 'Mega', 'Mercedes-Benz', 'MEV', 'MG', 'Micro-vett', 'MINI', 'Mitsubishi', 'Morgan', 'Nissan', 'NIU', 'Opel', 'Partner', 'Peugeot', 'Piaggio Vehículos comerciales', 'Piaggio Vespa', 'Polaris', 'Porsche', 'Quattro', 'REGARD', 'Renault', 'Renault Trucks', 'Rieju', 'RollsRoyce', 'Rover', 'Saab', 'Santana', 'Scania', 'SEAT', 'Silence', 'SKODA', 'Skoda Canarias', 'Smart', 'SsangYong', 'STORM', 'Subaru', 'SUKOY', 'Suzuki', 'Tata', 'TAZZARI', 'Tazzari EV', 'TOMBERLIN', 'Torrot', 'Toyota', 'Toyota Canarias', 'Vectia', 'VECTRIX', 'Volkswagen Canarias', 'Volkswagen Turismos', 'Volta Motorbikes', 'Volteis', 'Volvo', 'Volvo Trucks', 'XINYANG', 'ZD', 'ZERO MOTORCYCLES']`  
`Seleccion:`  

Debemos escribir una de las marcas de coches que nos propone. Los registros obtenidos se almacenaran en un archivo de tipo CSV.
