# ESTO SIRVE PARA CONECTAR LA BASE DE DATOS 
import mysql.connector  # IMPORTAMOS LO QUE HEMOS INSTALADO PIP INSTALL MYSQL.......

database = mysql.connector.connect( # LLAMAMOS AL FUNCION CONNECT PARA CONECTARNOS
    host ='127.0.0.1', #NUESTRO HOST, ESTA EN EL DOCKER COMPOSE
    port = 6033,
    user ='root', #USUARIO QUE USAMOS NOSOTROS
    password ='root', #CONTRASEÑA CON LA QUE NOS CONECTAMOS
    database='IES'
) 

print(database)