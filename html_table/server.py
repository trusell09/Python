from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/people")
def people():
    
    personal_info = [
        {'first': 'First Name', 'last' : 'Last Name'},
        {'first': 'Michael', 'last' : 'Choi'},
        {'first': 'John', 'last' : 'Supsupin'},
        {'first': 'Mark', 'last' : 'Guillen'},
        {'first': 'KB', 'last' : 'Tonel'}
    ]



    return render_template("index.html", names = personal_info)



if __name__=="__main__":
    app.run(debug=True) 
