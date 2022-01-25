from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'dsfsdfsdf'


@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        counter = session['counter']
    return render_template('index.html')

@app.route('/counter')
def counter():
    print(session)
    session['counter'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)