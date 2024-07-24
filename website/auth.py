from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        type = request.form.get('type')
        if type == 'signUp':
            nameSingUp = request.form.get('nameSingUp')
            emailSingUp = request.form.get('emailSingUp')
            password1SingUp = request.form.get('password1SingUp')
            password2SingUp = request.form.get('password2SingUp')

            if len(emailSingUp) < 4:
                flash("El email debe ser de 4 caracteres o mas", category='error')
            elif len(nameSingUp) < 2:
                flash("El nombre debe ser de 2 caracteres o mas", category='error')
            elif password1SingUp != password2SingUp:
                flash("Las contraseñas no son iguales", category='error')
            elif len(password1SingUp) < 7:
                flash("La contraseña debe ser de 7 caracteres o mas", category='error')
            else:
                flash("Cuenta creada", category='succes')
        else:
            pass


    data = request.form
    print(data)
    return render_template("login.html", user="Juan", boolean = False)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"
