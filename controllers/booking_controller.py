from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import datetime

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)

@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_booking():
    members = member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    return render_template("bookings/new.html", members = members, gym_classes = gym_classes)

@bookings_blueprint.route("/bookings",  methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    gym_class_id = request.form['gym_class_id']
    member = member_repository.select(member_id)
    gym_class = gym_class_repository.select(gym_class_id)
    # now = datetime.datetime.now()
    # if now.hour == 6 and now.minute == 20:
    #     print("It's 6:20!")
    booking = Booking(member, gym_class)
    booking_repository.save(booking)
    return redirect('/bookings')

@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_task(id):
    booking_repository.delete(id)
    return redirect('/bookings')