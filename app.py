from flask import Flask, render_template, request, redirect, session 
from flask_bcrypt import Bcrypt

from models.usuarios import Usuario
from models.tasks import Tasks 




app = Flask(__name__, static_folder='static', template_folder='templates')

app.secret_key = "P4S$W0rd"
bcrypt = Bcrypt(app)

@app.route("/", methods=["GET"])
def logout():
    return render_template('iniciosesion.html')

@app.route("/registrarse/", methods=["POST"])
def registrar():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    email = request.form.get("email")
    pass1 = request.form.get("pass1")
    pass2 = request.form.get("pass2")
    
    errors = []
    
    if not firstname or len("firstname") < 3:
        errors.append("Nombre invalido")
        
    if not lastname or len("lastname") < 3:
        errors.append("Apellido invalido")
        
    if not email or len("email") < 3:
        errors.append("Email invalido")
        
    if not pass1 == pass2:
        errors.append("La contraseña no coinciden")
    
    users = Usuario.select_correo(email)
    
    if len(errors) > 0: 
        return render_template("iniciosesion.html", registrarse_error=errors)
    
    pass1 = bcrypt.generate_password_hash(pass1).decode("utf-8")
    user = Usuario.insert_usuario(firstname, lastname, email, pass1)
    return redirect("/")

@app.route("/iniciosesion", methods=["POST"])
def iniciosesion():
    email = request.form.get("email")
    pass1 = request.form.get("password")
    
    errors = []
    
    user = Usuario.select_correo("email")
    
    if (len(user) == 0):
        errors.append("Email no registrado. Registrese por favor")
    else:
        user = user[0]
        if not bcrypt.check_password_hash(user.pass1, pass1):
            errors.append("El email y/o contraseña no corresponden")
            
    if len(errors) > 0:
        return render_template("paginaprincipal.html", login_errors=errors)
    
    
    session["id"] = user.id 
    session["firstname"] = f"{user.firstname}"
    
    return redirect("/")

@app.route("/iniciosesion/", methods=["GET"])
def loguo():
    session.clear()
    return redirect("paginaprincipal.html")


#


@app.route("/Inicionube/")
def inicio():
    return render_template('paginaprincipal.html')

@app.route('/citas/crear/', methods=["GET"])
def crear_citas():
    return render_template('crear_citas.html')
    
@app.route('/citas/crear/', methods=["POST", ])
def crear_cita():
    citas = request.form.get("nombre_citas")
    Tasks.insert(citas)
    return redirect('/Inicionube/')

if __name__ == '__main__':
    app.run(debug=True)