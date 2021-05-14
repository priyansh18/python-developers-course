from flask import Flask,render_template,redirect
from flask.globals import request

app = Flask(__name__)

fruits = ["Apple","Mango","Kiwi"]

num = 5

@app.route('/')
def hello():
    return render_template("index.html",allFruits = fruits,number = num )

@app.route('/submit',methods=['POST'])
def submit_data():
    if request.method == 'POST':
        # print(request.form)
        name = request.form['username']

        

    return "<h1>Hello {} </h1>".format(name)

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/home')
def home():
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)