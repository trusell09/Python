from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key ="l;sdknf"



@app.route('/')
def index():
    
    if "name" not in session:
        name = "Default User"
    else:
        name = session["name"]

    return render_template('index.html', name=name)


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    print(request.form["name"])
    print(request.form["email"])
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    
    #name =  request.form['name']
    email = request.form['email']
    vacation = request.form['vacation']    
    #session information directly above, session below and secret key at top

    
    session["name"] = request.form['name'] 
    
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)