from db.run_sql import run_sql
from models.gym_class import Gym_class
from models.member import Member

def save(member):
    sql = "INSERT INTO members( name, type ) VALUES ( %s, %s ) RETURNING id"
    values = [member.name, member.type]
    results = run_sql( sql, values )
    member.id = results[0]['id']
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['type'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['name'], result['type'], result['id'])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def gym_classes(member):
    gym_classes = []
    sql = "SELECT gym_classes.* FROM gym_classes INNER JOIN bookings ON bookings.gym_class_id = gym_classes.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        gym_class = Gym_class(row['name'], row['instructor'], row['date'], row['time'], row['duration'], row['capacity'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def update(member):
    sql = "UPDATE members SET (name, type) = (%s, %s) WHERE id = %s"
    values = [member.name, member.type, member.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE  FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

