from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/post", methods=['GET''POST'])
def post():
    if request.method == 'POST':
       name = request.form.get('name')
       email = request.form.get('emailaddress')
       phone_name = request.form.get('pone_number')
       name = request.form.get('message')

    return render_template('post.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')
app.run(debug=True)

