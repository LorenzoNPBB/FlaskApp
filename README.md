# FlaskApp

### Para iniciar la aplicación tenemos que tener instalado 

- **pip install flask**  --> para hacer la app
- **pip install mysql-connector-python==8.0.29** --> para hacer la conexión de nuestro python a la base de datos


Una vez iniciado (play) nos vamos al navegador e introducimos la ruta que nos proporciona. :+1:


Esta es la página principal de nuestra aplicación WEB.
En el puedes introducir el UsuarioAlumno, el Nombre y la Password para después darle a Guardar e introducir datos.
Estos datos ya introducidos los he metido directamente desde la página.
-------------------------------
![Introducción](https://images2.imgbox.com/e9/31/iARTcYlO_o.jpg "Página Principal")


Donde a su vez al hacer un SELECT * FROM IES salen los datos que ya hemos introducido.
-----------------------------------
![BaseDatos](https://images2.imgbox.com/4d/d6/GBYf84xb_o.jpg "BaseDatos")

También podemos modificar los datos desde la página web dando a EDIT en un registro.
-----------------------------------
![Edicion](https://images2.imgbox.com/d9/86/QEISl0pl_o.jpg "Edicion")

Una vez le demos a save changes nos modificará los cambios tanto en nuestra app como en la base de datos.
-----------------------------------
![Edicion](https://images2.imgbox.com/94/54/gvaR3MOL_o.jpg "Edicion")

Aquí el cambio en mi PhpMyAdmin
-----------------------------------
![Edicion](https://images2.imgbox.com/94/54/gvaR3MOL_o.jpg "Edicion")

Si le damos a Delete se nos borra tanto en nuestra app como en la base de datos.
-----------------------------------
![Borrar](https://images2.imgbox.com/79/b8/jOf7tECy_o.jpg "Borrar")

Aqui vemos que se ha borrado en la base de datos.
-----------------------------------
![Borrar](https://images2.imgbox.com/88/12/Fk9DxB0a_o.jpg "Borrar")


**En el repositorio dejo la carpeta con la app de Python**
**Y también el docker exportado con la base de datos**

