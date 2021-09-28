from db.run_sql import run_sql
from models.gym_class import Gym_class
from models.staff_member import Staff_Member

def save(staff_member):
    sql = "INSERT INTO staff_members( name, job_type ) VALUES ( %s, %s ) RETURNING id"
    values = [staff_member.name, staff_member.job_type]
    results = run_sql( sql, values )
    staff_member.id = results[0]['id']
    return staff_member

def select_all():
    list_of_staff = []

    sql = "SELECT * FROM staff_members"
    results = run_sql(sql)
    for result in results:
        staff = Staff_Member(result['name'], result['job_type'], result['id'])
        list_of_staff.append(staff)
    return list_of_staff

def select(id):
    staff_member = None
    sql = "SELECT * FROM staff_members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        staff_member = Staff_Member(result['name'], result['job_type'], result['id'])
    return staff_member

def delete_all():
    sql = "DELETE FROM staff_members"
    run_sql(sql)

def gym_classes(staff_member):
    gym_classes = []
    # sql = "SELECT gym_classes.* FROM gym_classes INNER JOIN bookings ON bookings.gym_class_id = gym_classes.id WHERE instructor = %s"
    sql = "SELECT gym_classes.* FROM gym_classes WHERE gym_classes.instructor = %s;"
    values = [staff_member.name]
    results = run_sql(sql, values)

    for row in results:
        gym_class = Gym_class(row['name'], row['instructor'], row['date'], row['time'], row['duration'], row['capacity'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def update(staff_member):
    sql = "UPDATE staff_members SET (name, job_type) = (%s, %s) WHERE id = %s"
    values = [staff_member.name, staff_member.job_type, staff_member.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE  FROM staff_members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM staff_members"
    run_sql(sql)

