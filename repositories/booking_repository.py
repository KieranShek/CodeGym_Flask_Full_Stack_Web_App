from db.run_sql import run_sql
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import pdb

def save(booking):
    sql = "INSERT INTO bookings ( member_id, gym_class_id ) VALUES ( %s, %s) RETURNING id;"
    values = [booking.member.id, booking.gym_class.id]
    # check_capacity = f"select count(*) from bookings where gym_class_id = {booking.gym_class.id};"
    # checked_capacity = run_sql(check_capacity)
    # if checked_capacity[0][0] > booking.gym_class.capacity:
    #     return None
    # else:
    check_capacity(booking)
    results = run_sql( sql, values )
    booking.id = results[0]['id']
    return booking

def check_capacity(booking):
    check_capacity = f"select count(*) from bookings where gym_class_id = {booking.gym_class.id};"
    checked_capacity = run_sql(check_capacity)
    empty_list = []
    empty_list.append(checked_capacity[0][0])
    if checked_capacity[0][0] >= booking.gym_class.capacity:
        empty_list.append("Full")
        return empty_list
    else:
        empty_list.append("Spaces")
        return empty_list

def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        gym_class = gym_class_repository.select(row['gym_class_id'])
        booking = Booking(member, gym_class, row['id'])
        bookings.append(booking)
    return bookings

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)
