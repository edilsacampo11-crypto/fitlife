from flask import Flask, render_template, request, flash 
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('FLASK_SECRET_KEY', '2110')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        nombre = request.form['nombre']
        correo = request.form['correo']
        membresia = request.form['membresia_escogida']

        # Crear el mensaje de correo
        msg = Message('Nueva Solicitud de Membresia',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[app.config['MAIL_USERNAME']])
        msg.body = f"Nombre:{nombre}\nCorreo: {correo}\nMembresia Escogida:{membresia}"

        # Enviar el mensaje
        mail.send(msg)
        flash("Mensaje enviado correctamente.")
    except Exception as e:
        print(f"Error:{e}")
        flash("Ocurrio un error al enviar el mensaje. Intenta de nuevo mas tarde. ")

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)



