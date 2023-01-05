from flask import Flask, render_template, request, redirect, url_for
import os  # PARA PODER ACCEDER A LOS DIRECTORIOS DE UNA MANERA FÁCIL 
import database as db # IMPORTAMOS EL ARCHIVO DATABASE PARA PODER ACCEDER A LA BASE DE DATOS

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # ESTO NOS SIRVE PARA ACCEDER A LA CARPETA DEL PROYECTO ABSOLUTO
template_dir = os.path.join(template_dir,'src','templates') # ESTO SIRVE PARA UNIR LA CARPETA SRC Y TEMPLATES AL PROYECTO

app = Flask(__name__, template_folder = template_dir) # ESTO ES PARA INICIAR LA APLICACIÓN, EL TEMPLATE_FOLDER ES LA DIRECCION QUE INDICAMOS ANTES



# RUTAS DE LA APLICACIÓN 

@app.route('/')  # ESTO ES LA RUTA PRINCIPAL DE NUESTRA APP SE PONE CON LA BARRA
def home():
    cursor = db.database.cursor() # PARA ACCEDER A LA BD
    cursor.execute("SELECT * FROM IES") # PARA OBTENER TODOS LOS DATOS DE LA BD QUE VAMOS A VER EN NUESTRO INDEX
    myresult = cursor.fetchall()  #PARA ACCEDER A TODOS LOS DATOS
    #CONVERTIR TODOS LOS DATOS A DICCIONARIO.
    insertObject = [] # AQUI VAN GUARDADAS LAS CLAVES DE LAS COLUMNAS
    columnNames = [column[0] for column in cursor.description] # PARA OBTENER LOS NOMBRES DE LAS COLUMNAS
    for record in myresult: # CON UN BUCLE DENTRO DE MYRESULT EXTRAIGO TODA LA INFORMACION 
        insertObject.append(dict(zip(columnNames,record))) # PARA IR METIENDO TODOS LOS DATOS EN FORMATO DICCIONARIO CON EL DICT. LA FUNCION ZIP ES PORQUE VAMOS A USAR COLUMN Y RECORD
    cursor.close() # PARA CERRAR EL CURSOR

    return render_template('index.html', data=insertObject)  # PARA QUE SALGA NUESTRO INDEX AL INICIO #DATA=INSERTOBJECT ES PARA QUE NOS SALGA EN NUESTRO HTML

#INDICAMOS EL NOMBRE DE LA RUTA GUARDAR USUARIOS EN LA BASE DE DATOS
@app.route('/user', methods=['POST'])
def addUser():
    UsuarioAlumno = request.form['UsuarioAlumno'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE DE USUARIO QUE INDIQUEMOs
    Nombre = request.form['Nombre'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE QUE INDIQUEMOS
    Password = request.form['Password'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL password QUE INDIQUEMOS

    if UsuarioAlumno and Nombre and Password: # ESTA CONDICION SIRVE PARA QUE SI TENEMOS TODOS LOS CAMPOS VAMOS A HACER LA CONSULTA INSERT A LA BASE DE DATOS
        cursor = db.database.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
        sql = "INSERT INTO IES (UsuarioAlumno,Nombre,Password) VALUES (%s, %s, %s)" # DEFINIMOS LA CONSULTA INSERT DE TIPO STRING %S
        data = (UsuarioAlumno,Nombre,Password) # HACEMOS UNA TUPLA CON LOS DATOS 
        cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
        db.database.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO
    return redirect(url_for('home')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK

@app.route('/delete/<string:CodigoAlumno>')
def delete(CodigoAlumno):
    cursor = db.database.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
    sql = "DELETE FROM IES WHERE CodigoAlumno=%s"
    data = (CodigoAlumno,) # HACEMOS UNA TUPLA CON LOS DATOS 
    cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
    db.database.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO
    return redirect(url_for('home')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK


@app.route('/edit/<string:CodigoAlumno>', methods=['POST'])
def edit (CodigoAlumno):
    UsuarioAlumno = request.form['UsuarioAlumno'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE DE USUARIO QUE INDIQUEMOs
    Nombre = request.form['Nombre'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE QUE INDIQUEMOS
    Password = request.form['Password'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL password QUE INDIQUEMOS

    if UsuarioAlumno and Nombre and Password: # ESTA CONDICION SIRVE PARA QUE SI TENEMOS TODOS LOS CAMPOS VAMOS A HACER LA CONSULTA INSERT A LA BASE DE DATOS
        cursor = db.database.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
        sql = "UPDATE IES SET UsuarioAlumno = %s, Nombre = %s, Password = %s WHERE CodigoAlumno = %s"# DEFINIMOS LA CONSULTA UPDATE EN LOS SIGUIENTES CAMPOS
        data = (UsuarioAlumno,Nombre,Password,CodigoAlumno) # HACEMOS UNA TUPLA CON LOS DATOS 
        cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
        db.database.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO
    return redirect(url_for('home')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK

if __name__ == '__main__':
    app.run(debug=True,port=4000) # ESTO SIRVE PARA PONER EL MODO DEBUG EN ON Y NO TENER QUE ESTAR CERRANDO Y ABRIENDO EL SERVIDOR. LO INICIALIZO EN EL PUERTO 4000 PARA PROBAR.

