from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route("/add/recipe")
def add_recipe():
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id":session["user_id"]
    }
    return render_template("new_recipe.html",user=User.get_by_id(data))

@app.route("/new/recipe",methods=["POST"])
def new_recipe():
    if "user_id" not in session:
        return redirect("/")
    if not Recipe.validate(request.form):
        return redirect("/add/recipe")
    data = {
        "user_id": session["user_id"],
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30min": int(request.form["under30min"]),
        "date_made": request.form["date_made"]
    }
    Recipe.add(data)
    return redirect("/dashboard")

@app.route("/show/recipe/<int:id>")
def show_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id":id
    }
    user_data = {
        "id":session["user_id"]
    }
    return render_template("show_recipe.html",recipe=Recipe.get_by_id(data),user=User.get_by_id(user_data))

@app.route("/edit/recipe/<int:id>")
def edit_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id":id
    }
    user_data = {
        "id":session["user_id"]
    }
    return render_template("edit_recipe.html",edit=Recipe.get_by_id(data),user=User.get_by_id(user_data))

@app.route("/delete/recipe/<int:id>")
def delete_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id":id
    }
    Recipe.delete(data)
    return redirect("/dashboard")

@app.route("/update/recipe",methods=["POST"])
def update_recipe():
    if "user_id" not in session:
        return redirect("/")
    if not Recipe.validate(request.form):
        return redirect("/add/recipe")
    data = {
        "id": request.form["id"],
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30min": int(request.form["under30min"]),
        "date_made": request.form["date_made"]
    }
    Recipe.update(data)
    return redirect("/dashboard")