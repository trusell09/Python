from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)


@app.route('/<name>')
def index(name):
    print(f"the name is: {name}")
    return render_template('index.html', name=name, num=8)

@app.route("/advanced")
def advanced():
    
    student_info = [
        {'name': 'Jimbo', 'age' : 37},
        {'name': 'Mimbo', 'age' : 27},
        {'name': 'Pimbo', 'age' : 17},
        {'name': 'Gimbo', 'age' : 7},
    ]


    return render_template("adv.html", students = student_info)


@app.route("/httpresponse")
def http():
    return "This is a Http Response"



if __name__=="__main__":
    app.run(debug=True)
