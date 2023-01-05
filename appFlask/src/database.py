# ESTO SIRVE PARA CONECTAR LA BASE DE DATOS 
import mysql.connector  # IMPORTAMOS LO QUE HEMOS INSTALADO PIP INSTALL MYSQL.......

database = mysql.connector.connect( # LLAMAMOS AL FUNCION CONNECT PARA CONECTARNOS
    host ='bedloyakthiprmt8t1rp-mysql.services.clever-cloud.com', #NUESTRO HOST, ESTA EN EL DOCKER COMPOSE
    port = 3306,
    user ='uunuupj7teqg6hj3', #USUARIO QUE USAMOS NOSOTROS
    password ='ujn3Z5419yw87xmlIZzZ', #CONTRASEÑA CON LA QUE NOS CONECTAMOS
    database='bedloyakthiprmt8t1rp'
) 

print(database)