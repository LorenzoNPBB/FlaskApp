from flask import Flask, render_template , redirect, url_for  # ESTO SIRVE PARA IMPORTAR FLASK. # RENDER_TEMPLATE ES PARA IMPORTAR HTMLS
from forms import TareaForm

#INSTALAR PIP FLASK-WTF

app = Flask (__name__) # ESTO ES PARA CREAR UNA INSTANCIA ; CUANDO QUERAMOS ACCEDER A UN ARCHIVO BUSCA EN __NAME__ ; SIEMPRE VA AHI 


app.secret_key = "hola"


"""@app.route("/") # ESTO ES PARA DEFINIR LA RUTA. A ESTO SE LE LLAMA DECORADOR. PARA EXTENDER LA FUNCIONALIDAD DE UNA FUNCION ; ESTO ES LO QUE EL USUARIO TIENE QUE PONER PARA VER LA APP SI PONEMOS /HOLA TENDRÁ QUE PONER 127.0.0.1:5000/HOLA
def index(): # ESTA RUTA LA LIGAMOS A LA SIGUIENTE FUNCION.
    return "Hola mundo!"""

tareas = ["Hacer la compra" , "Sacar al perro"]

@app.route("/", methods=["GET","POST"]) # ESTA ES NUESTRA CABECERA
def index():
    return render_template("index.html", tareas=tareas) # CON EL RENDER_TEMPLATE SELECCIONAMOS COMO RUTA PRINCIPAL EL INDEX.HTML

#### ESTA LINEA SIRVE PARA ACTIVAR EL MODO DEBUG DE FORMA FACIL Y QUE CADA VEZ QUE HAGAMOS UN CAMBIO SE CAMBIE AUTOMATICAMENTE AL REFRESCAR LA APP
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/agregar/" , methods=["GET","POST"])
def agregar():
    form = TareaForm()
    if form.validate_on_submit(): # REVISAR SI EL FORMULARIO ES VALIDO
        tarea = form.tarea.data
        tareas.append(tarea)
        return redirect(url_for('index'))
    return render_template("agregar.html", form=form)

### EJEMPLO SI PONES LA RUTA 127.0.0.1:5000/starwars + /STARWARS TE CARGA ESO
"""@app.route("/starwars/")
def starwars():
    return "Soy tu padreeeee"""

### ESTO ES PARA HACER RUTAS DINÁMICAS
"""@app.route("/<string:nombre>/")
def saludo(nombre):
    return f"Hola, {nombre}"""

## PARA PONER UNA VARIABLE COMO RUTA DINAMICA. ES EL HTML SALUDO. ############ ERA UNA PRUEBA ############
"""@app.route("/<string:nombre>/")
def saludo(nombre):
    return render_template("saludo.html", name=nombre)"""


