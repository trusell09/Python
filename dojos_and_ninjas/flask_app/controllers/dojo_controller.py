from flask import render_template, request, redirect, session

from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/dojos')
def dojos():
    dojos=Dojo.get_all()
    return render_template('dojos.html', all_dojos=dojos)

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data={
        'id':id
    }
    dojo=Dojo.get_one(data)
    print(dojo)
    return render_template('dojo_show.html', dojo=dojo)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    data={
        'dojo_name':request.form['dojo_name']
    }
    Dojo.add_new(data)
    return redirect('/dojos')