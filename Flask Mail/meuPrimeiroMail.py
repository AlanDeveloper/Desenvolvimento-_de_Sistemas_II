from flask import Flask, render_template, request
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

@app.route("/")
def index():
    return render_template('text.html')

@app.route("/send", methods=['POST'])
def send():
    msg = Message()
    msg.subject = request.form.get('title')
    msg.recipients= ['mauricio.bilhalva.freitas@gmail.com']
    msg.html = render_template('message.html', msg=request.form.get('msg'))
    msg.attach("image.png", "image/png", app.open_resource('gumball.png').read())

    thr = Thread(target=send_mail, args=[app, msg])
    thr.start()
    return "Sent"

def send_mail(app, msg):
    with app.app_context():
        mail.send(msg)

if __name__ == '__main__':
   app.run(debug=True)
