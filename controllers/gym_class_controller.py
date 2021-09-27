from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import Gym_class
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
import pdb

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
    date = request.form['date']
    time = request.form['time']
    duration = request.form['duration']
    gym_class = Gym_class(name, category, date, time, duration)
    gym_class_repository.save(gym_class)
    return redirect('/gym_classes')

@gym_classes_blueprint.route("/gym_classes/<id>/edit", methods=['GET'])
def update_class(id):
    gym_class = gym_class_repository.select(id)
    return render_template("gym_classes/edit.html", gym_class = gym_class)

@gym_classes_blueprint.route("/gym_classes/<id>",  methods=['POST'])
def edit_class(id):
    id = id
    name = request.form['class_name']
    category = request.form['category']
    date = request.form['date']
    time = request.form['time']
    duration = request.form['duration']
    gym_class = Gym_class(name, category, date, time, duration, id)
    gym_class_repository.update(gym_class)
    return redirect('/gym_classes')

@gym_classes_blueprint.route("/gym_classes/<id>/delete", methods=['POST'])
def delete_class(id):
    gym_class_repository.delete(id)
    return redirect('/gym_classes')