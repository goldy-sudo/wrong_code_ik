from flask import * 
from flask_mail import Message, Mail
from random import * 

app = Flask(__name__)
otp = randint(00000,99999)

app.config['SERVER_FLASK_MAIL'] = 'smtp.gmail.com'
app.config['MAIL_NAME'] = 'YOUR EMAIL @gmail.com' #YOUR EMAIL @gmail.com
app.config['MAIL_PASSWORD'] = 'YOUR APP PASSWORD ' #YOUR APP PASSWORD 
app.config['MAIL_PORT'] = 443 
app.config['MAIL_USE_TLS'] = True 
app.config['MAIL_USE_SSL'] = False 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/savecred', methods=['GET','POST'])
def savecred():
    if request.method == 'POST':
        if  request.form.get('email') != 'foligolu09@gamil.com' and request.form.get('password') != '123':
            return render_template('home.html')
        else:
            email = request.form.get('email')
            password = request.form.get('password')
            
        return render_template('showvals.html', email=email, password=password)

@app.route('/malepage')
def malepage():
    return render_template


if __name__ == '__main__':
    app.run(debug=True)








    
#tls port = 443
#ssl port = try 587