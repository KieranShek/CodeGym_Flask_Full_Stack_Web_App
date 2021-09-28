from db.run_sql import run_sql
from models.gym_class import Gym_class
from models.member import Member

def save(gym_class):
    sql = "INSERT INTO gym_classes(name, category, date, time, duration, capacity) VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [gym_class.name, gym_class.category, gym_class.date, gym_class.time, gym_class.duration, gym_class.capacity]
    results = run_sql( sql, values )
    gym_class.id = results[0]['id']
    return gym_class

# def check_capacity(gym_class):
#     check_capacity = f"select count(*) from bookings where gym_class_id = {gym_class.id};"
#     checked_capacity = run_sql(check_capacity)
#     empty_list = []
#     empty_list.append(checked_capacity[0][0])
#     if checked_capacity[0][0] >= gym_class.capacity:
#         empty_list.append("Full")
#         return empty_list
#     else:
#         empty_list.append("Spaces")
#         return empty_list


def select_all():
    gym_classes = []

    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)

    for row in results:
        gym_class = Gym_class(row['name'], row['category'], row['date'], row['time'], row['duration'], row['capacity'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes


def select(id):
    gym_class = None
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_class = Gym_class(result['name'], result['category'], result['date'], result['time'], result['duration'], result['capacity'], result['id'] )
    return gym_class


def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)


def members(gym_class):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE gym_class_id = %s"
    values = [gym_class.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row['type'])
        members.append(member)
    return members

def update(gym_class):
    sql = "UPDATE gym_classes SET (name, category, date, time, duration, capacity) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [gym_class.name, gym_class.category, gym_class.date, gym_class.time, gym_class.duration, gym_class.capacity, gym_class.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM gym_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)