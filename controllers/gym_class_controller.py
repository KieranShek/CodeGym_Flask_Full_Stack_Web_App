from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import Gym_class
import repositories.gym_class_repository as gym_class_repository

gym_classes_blueprint = Blueprint("gym_classes", __name__)

@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repository.select_all() 
    return render_template("gym_classes/index.html", gym_classes = gym_classes)

@gym_classes_blueprint.route("/gym_classes/<id>")
def show(id):
    gym_class = gym_class_repository.select(id)
    members = gym_class_repository.members(gym_class)
    return render_template("gym_classes/show.html", members=members, gym_class = gym_class)

@gym_classes_blueprint.route("/gym_classes/new", methods=['GET'])
def new_class():
    gym_class = gym_class_repository.select_all()
    return render_template("gym_classes/new.html", gym_class = gym_class)

@gym_classes_blueprint.route("/gym_classes",  methods=['POST'])
def create_task():
    name = request.form['class_name']
    category = request.form['category']
    gym_class = Gym_class(name, category)
    gym_class_repository.save(gym_class)
    return redirect('/gym_classes')
