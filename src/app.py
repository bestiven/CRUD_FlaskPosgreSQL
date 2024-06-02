
from flask import Flask, render_template,request,redirect,url_for
from config import *

con_bd = establecerconexion()

app= Flask(__name__)

@app.route('/')
def index():
    cursor =con_bd.cursor()
    sql = "SELECT*FROM personas"
    cursor.execute(sql)
    PersonasRegistradas = cursor.fetchall()
    return render_template('index.html' , personas=PersonasRegistradas)


@app.route('/guardar_personas', methods=['POST'])
def agregarPersona():
    cursor = con_bd.cursor()
    nombre =request.form['nombre']
    apellido =request.form['apellido']
    telefono =request.form['telefono']

    if nombre and apellido and telefono :
        sql ="""
            INSERT INTO personas (nombre,apellido,telefono) 
            VALUES (%s, %s, %s)
            """
        cursor.execute(sql,(nombre,apellido,telefono))
        con_bd.commit()
        return redirect(url_for('index'))
    else :
        return "Error de consulta"
    

@app.route("/editar_persona/<int:id_persona>", methods=["POST"])
def editar(id_persona):
    cursor = con_bd.cursor()
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    telefono = request.form["telefono"]

    if nombre and apellido and telefono:
        sql = """
            UPDATE personas
            SET nombre=%s, apellido=%s, telefono=%s 
            WHERE id=%s"""
        cursor.execute(sql, (nombre, apellido, telefono, id_persona))
        con_bd.commit()
        return redirect(url_for("index"))
    else:
        return "Error en la consulta"
    
@app.route('/eliminar_persona/<int:id_persona>')
def eliminar(id_persona):
    cursor =con_bd.cursor()
    sql ="DELETE FROM personas WHERE id = {0}".format(id_persona)
    cursor.execute(sql)
    con_bd.commit()
    return redirect(url_for('index'))
    
def crearTablaPersonas():
    cursor=con_bd.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS personas(
                       id serial NOT NULL,
                       nombre character varying(30),
                       apellido character varying(30),
                       telefono character varying(10),
                       CONSTRAINT pk_personas_id PRIMARY KEY (id)
                       );
                       """)
    con_bd.commit()
    
    
if __name__=='__main__':
    crearTablaPersonas()
    app.run(debug=True)