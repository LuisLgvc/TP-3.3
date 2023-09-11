# TP-3.3

El json recomendado para probar el funcionamiento de todos los endpoints es:
{
  "description": "Nueva descripción",
  "language_id": 1,
  "length": 86,
  "original_language_id": null,
  "rating": "PG",
  "release_year": 2006,
  "rental_duration": 6,
  "rental_rate": 0.99,
  "replacement_cost": 20.99,
  "special_features": [
    "Behind the Scenes",
    "Deleted Scenes"
  ],
  "title": "Nuevo título"
}
Se recomienda usar ThunderClient(extension de Visual Studio Code) y colocar el json en la pestaña de body y JSON respectivamente a su vez de colocar los endpoints para cada ejercicio:

# Ejercicio 1 'GET'
http://127.0.0.1:5000/films/20

# Ejercicio 2 'POST'
http://127.0.0.1:5000/films/films

# Ejercicio 3 'PUT'
http://127.0.0.1:5000/films/100

# Ejercicio 4 'PUT'
http://127.0.0.1:5000/films/100

# Ejercicio 5 'DELETE' 
Se recomienda hacer aunque sea un ingreso ya que la tabla de la base de datos no permite borrar los datos existentes
http://127.0.0.1:5000/films/1001


Comentarios: Se solucionaron los errores que habian, se producian en el area de validacion y en el orden de llamado a la funcion de validacion en los controladores

//////////////////
En caso de no funcionar o de arrojar un error sobre dotenv:
Se recomienda verificar si se lo tiene instalado y a su vez actualizar la version de mysql-connector con el comando: pip install --upgrade mysql-connector-python
Todo esto corriendo sobre un entorno virtual previamente creado y que cuenta con todos los paquetes necesarios para el funcionamiento de la api (mysql-connector, flask, flask_cors, python-dotenv); comandos: pip install flask, pip install python-dotenv, pip install flask-cors, pip install mysql-connector