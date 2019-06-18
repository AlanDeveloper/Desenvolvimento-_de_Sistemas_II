from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
from threading import Thread

app = Flask(__name__, template_folder='template')
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'genicandogenerico@gmail.com'
app.config['MAIL_PASSWORD'] = 'adm@123abc'
app.config['MAIL_DEFAULT_SENDER'] = 'genicandogenerico@gmail.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def reg():
    msg = Message()
    msg.subject = 'Confirmação de e-mail'
    msg.recipients = [request.form.get('email')]
    msg.html = render_template('message.html')

    thr = Thread(target=send_mail, args=[app, msg])
    thr.start()

    status = request.form.get('email')
    if (status != ''):
        status = 'E-mail enviado com sucesso'
    return redirect('/')

def send_mail(app, msg):
    with app.app_context():
        mail.send(msg)

@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/feed')
def feed():
        return render_template('feed.html')

if __name__ == '__main__':
   app.run(debug=True)
