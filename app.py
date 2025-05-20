# Importamos las bibliotecas necesarias de Flask
from flask import Flask, render_template, request, redirect, url_for, session

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Clave secreta necesaria para usar sesiones (como login)
app.secret_key = 'clave_secreta_segura'

# Diccionario que simula una base de datos de usuarios
users = {
    'admin': {'password': 'admin123', 'email': 'admin@example.com'}
}

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')  # Renderiza la plantilla index.html

# Ruta para el login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # Si el formulario fue enviado
        username = request.form['username']  # Captura el nombre de usuario
        password = request.form['password']  # Captura la contraseña
        user = users.get(username)  # Busca el usuario en el "diccionario"

        # Si el usuario existe y la contraseña es correcta
        if user and user['password'] == password:
            session['username'] = username  # Guarda el login en la sesión
            return redirect(url_for('dashboard'))  # Redirige al dashboard
        else:
            return "Credenciales inválidas", 403  # Error si no coincide

    return render_template('login.html')  # Si es GET, muestra el formulario

# Ruta para el panel principal (dashboard)
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:  # Si no está logueado, redirige al login
        return redirect(url_for('login'))
    return render_template('dashboard.html', users=users)  # Muestra usuarios

# Ruta para editar un usuario específico
@app.route('/edit/<username>', methods=['GET', 'POST'])
def edit_user(username):
    if 'username' not in session:  # Verifica que esté logueado
        return redirect(url_for('login'))

    user = users.get(username)  # Obtiene los datos del usuario
    if not user:
        return "Usuario no encontrado", 404  # Error si no existe

    if request.method == 'POST':  # Si el formulario fue enviado
        new_email = request.form['email']  # Obtiene el nuevo email
        new_password = request.form['password']  # Nueva contraseña (si hay)
        user['email'] = new_email  # Actualiza el email
        if new_password:  # Si se ingresó nueva contraseña, la actualiza
            user['password'] = new_password
        return redirect(url_for('dashboard'))  # Regresa al dashboard

    # Si es GET, muestra el formulario de edición
    return render_template('edit_user.html', username=username, user=user)

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.clear()  # Borra toda la información de sesión (logout)
    return redirect(url_for('index'))  # Vuelve a la página de inicio

# Lanza la aplicación si ejecutamos el script directamente
if __name__ == '__main__':
    app.run(debug=True)  # Activa el modo debug (útil para desarrollo)
