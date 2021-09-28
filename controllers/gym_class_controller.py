from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import Gym_class
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository
import repositories.staff_member_repository as staff_member_repository
from datetime import datetime
import pdb


gym_classes_blueprint = Blueprint("gym_classes", __name__)

@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    capacities = []
    instructors = staff_member_repository.select_all()
    gym_classes = gym_class_repository.select_all() 
    for gym_class in gym_classes:
        capacities.append(gym_class_repository.check_capacity(gym_class))
    return render_template("gym_classes/index.html", gym_classes = gym_classes, capacities = capacities, instructors = instructors)

@gym_classes_blueprint.route("/gym_classes/<id>")
def show(id):
    capacities = []
    gym_class = gym_class_repository.select(id)
    members = gym_class_repository.members(gym_class)
    instructors = staff_member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    capacities.append(gym_class_repository.check_capacity(gym_class))
    return render_template("gym_classes/show.html", members=members, gym_class = gym_class, gym_classes=gym_classes, capacities=capacities, instructors = instructors)

@gym_classes_blueprint.route("/gym_classes/new", methods=['GET'])
def new_class():
    gym_class = gym_class_repository.select_all()
    staff_members = staff_member_repository.select_all()
    return render_template("gym_classes/new.html", gym_class = gym_class, staff_members = staff_members)

@gym_classes_blueprint.route("/gym_classes",  methods=['POST'])
def create_task():
    name = request.form['class_name']
    instructor = request.form['instructor']
    date = request.form['date']
    time = request.form['time']
    duration = request.form['duration']
    capacity = request.form['capacity']
    gym_class = Gym_class(name, instructor, date, time, duration, capacity)
    gym_class_repository.save(gym_class)
    return redirect('/gym_classes')

@gym_classes_blueprint.route("/gym_classes/<id>/edit", methods=['GET'])
def update_class(id):
    gym_class = gym_class_repository.select(id)
    staff_members = staff_member_repository.select_all()
    return render_template("gym_classes/edit.html", gym_class = gym_class, staff_members = staff_members)

@gym_classes_blueprint.route("/gym_classes/<id>",  methods=['POST'])
def edit_class(id):
    id = id
    name = request.form['class_name']
    instructor = request.form['instructor']
    date = request.form['date']
    time = request.form['time']
    duration = request.form['duration']
    capacity = request.form['capacity']
    gym_class = Gym_class(name, instructor, date, time, duration, capacity, id)
    gym_class_repository.update(gym_class)
    return redirect('/gym_classes')

@gym_classes_blueprint.route("/gym_classes/<id>/delete", methods=['POST'])
def delete_class(id):
    gym_class_repository.delete(id)
    return redirect('/gym_classes')

@gym_classes_blueprint.route("/gym_classes/<class_id>/<member_id>/delete", methods=['POST'])
def delete_from_class(class_id, member_id):
    id = gym_class_repository.find_booking_id(int(class_id), int(member_id))
    booking_repository.delete(id[0])
    return redirect('/gym_classes')