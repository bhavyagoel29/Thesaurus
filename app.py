from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if request.method=='POST':
        print(request.form['username'])
        print(request.form['password'])
    return render_template('home.html')

app.run(debug=True)