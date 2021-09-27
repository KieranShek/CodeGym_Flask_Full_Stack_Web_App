from db.run_sql import run_sql
from models.gym_class import Gym_class
from models.member import Member

def save(gym_class):
    sql = "INSERT INTO gym_classes(name, category, date, time, duration) VALUES ( %s, %s, %s, %s, %s ) RETURNING id"
    values = [gym_class.name, gym_class.category, gym_class.date, gym_class.time, gym_class.duration]
    results = run_sql( sql, values )
    gym_class.id = results[0]['id']
    return gym_class


def select_all():
    gym_classes = []

    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)

    for row in results:
        gym_class = Gym_class(row['name'], row['category'], row['date'], row['time'], row['duration'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes


def select(id):
    gym_class = None
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_class = Gym_class(result['name'], result['category'], result['date'], result['time'], result['duration'], result['id'] )
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
        member = Member(row['name'])
        members.append(member)
    return members

def update(gym_class):
    sql = "UPDATE gym_classes SET (name, category, date, time, duration) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [gym_class.name, gym_class.category, gym_class.date, gym_class.time, gym_class.duration, gym_class.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM gym_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)