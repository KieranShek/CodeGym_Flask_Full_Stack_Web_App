from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.staff_member import Staff_Member
import repositories.staff_member_repository as staff_member_repository
import pdb

staff_members_blueprint = Blueprint("staff_members", __name__)

@staff_members_blueprint.route("/staff_members")
def staff_members():
    staff_members = staff_member_repository.select_all()
    return render_template("staff_members/index.html", staff_members = staff_members)

@staff_members_blueprint.route("/staff_members/<id>")
def show(id):
    staff_member = staff_member_repository.select(id)
    gym_classes = staff_member_repository.gym_classes(staff_member)
    # pdb.set_trace()
    return render_template("staff_members/show.html", staff_member = staff_member, gym_classes = gym_classes)

@staff_members_blueprint.route("/staff_members/new", methods=['GET'])
def new_staff_member():
    staff_members = staff_member_repository.select_all()
    return render_template("staff_members/new.html", staff_members = staff_members)

@staff_members_blueprint.route("/staff_members",  methods=['POST'])
def create_staff_member():
    name = request.form['staff_member_name']
    job_type = request.form['job_type']
    staff_member = Staff_Member(name, job_type)
    staff_member_repository.save(staff_member)
    return redirect('/staff_members')

@staff_members_blueprint.route("/staff_members/<id>/edit", methods=['GET'])
def update_staff_member(id):
    staff_member = staff_member_repository.select(id)
    return render_template("staff_members/edit.html", staff_member = staff_member)

@staff_members_blueprint.route("/staff_members/<id>",  methods=['POST'])
def edit_staff_member(id):
    name = request.form['staff_member_name']
    job_type = request.form['job_type']
    staff_member = Staff_Member(name, job_type, id)
    staff_member_repository.update(staff_member)
    return redirect('/staff_members')

@staff_members_blueprint.route("/staff_members/<id>/delete", methods=['POST'])
def delete_staff_member(id):
    staff_member_repository.delete(id)
    return redirect('/staff_members')
