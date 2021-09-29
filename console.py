# from CodeGym.models.staff_member import Staff_Member
import pdb
from models.gym_class import Gym_class
from models.member import Member
from models.booking import Booking
from models.staff_member import Staff_Member

import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository
import repositories.staff_member_repository as staff_member_repository

booking_repository.delete_all()
gym_class_repository.delete_all()
member_repository.delete_all()
staff_member_repository.delete_all()

member1 = Member('Jack', 'Premium')
member_repository.save(member1)

member2 = Member('John', 'Premium')
member_repository.save(member2)

member3 = Member('Gerald', 'Premium')
member_repository.save(member3)

member4 = Member('Carlos', 'Standard')
member_repository.save(member4)

member5 = Member('David', 'Standard')
member_repository.save(member5)

member6 = Member('Andrew', 'Premium')
member_repository.save(member6)

member7 = Member('Ian', 'Premium')
member_repository.save(member7)

member8 = Member('Lewis', 'Premium')
member_repository.save(member8)

member9 = Member('Morven', 'Standard')
member_repository.save(member9)

member10 = Member('Callum', 'Premium')
member_repository.save(member10)

member11 = Member('Vinnie', 'Standard')
member_repository.save(member11)

member12 = Member('Willem', 'Standard')
member_repository.save(member12)

member13 = Member('Tony', 'Premium')
member_repository.save(member13)

member14 = Member('Athina', 'Premium')
member_repository.save(member14)

member15 = Member('Neil', 'Premium')
member_repository.save(member15)

member16 = Member('Andrew', 'Standard')
member_repository.save(member16)

member17 = Member('Lucinda', 'Premium')
member_repository.save(member17)

member18 = Member('Jordan', 'Premium')
member_repository.save(member18)

member19 = Member('Craig', 'Premium')
member_repository.save(member19)

member20 = Member('Janice', 'Standard')
member_repository.save(member20)

member21 = Member('Alex', 'Premium')
member_repository.save(member21)

gym_class1 = Gym_class('Spin Class', 1, '2021-09-01', '09:00', 45, 10)
gym_class_repository.save(gym_class1)

gym_class2 = Gym_class('Leg Day', 2, '2021-09-01', '09:00', 60, 8)
gym_class_repository.save(gym_class2)

gym_class3 = Gym_class('Arm Day', 3, '2021-08-30', '12:00', 60, 12)
gym_class_repository.save(gym_class3)

staff1 = Staff_Member('Steve', 'Instructor')
staff_member_repository.save(staff1)

staff2 = Staff_Member('Stan', 'Instructor')
staff_member_repository.save(staff2)

staff3 = Staff_Member('Jen', 'Instructor')
staff_member_repository.save(staff3)

staff4 = Staff_Member('Craig', 'Instructor')
staff_member_repository.save(staff4)

staff5 = Staff_Member('Pete', 'Instructor')
staff_member_repository.save(staff5)

booking1 = Booking(member1, gym_class2)
booking_repository.save(booking1)

booking2 = Booking(member2, gym_class2)
booking_repository.save(booking2)

booking3 = Booking(member3, gym_class2)
booking_repository.save(booking3)

booking4 = Booking(member4, gym_class2)
booking_repository.save(booking4)

booking5 = Booking(member5, gym_class2)
booking_repository.save(booking5)

booking6 = Booking(member6, gym_class3)
booking_repository.save(booking6)

booking7 = Booking(member7, gym_class3)
booking_repository.save(booking7)

booking8 = Booking(member8, gym_class3)
booking_repository.save(booking8)

booking9 = Booking(member9, gym_class2)
booking_repository.save(booking9)

booking10 = Booking(member10, gym_class3)
booking_repository.save(booking10)

booking11 = Booking(member10, gym_class1)
booking_repository.save(booking11)

booking12 = Booking(member11, gym_class1)
booking_repository.save(booking12)

booking13 = Booking(member11, gym_class2)
booking_repository.save(booking13)

booking14 = Booking(member12, gym_class1)
booking_repository.save(booking14)

booking15 = Booking(member12, gym_class3)
booking_repository.save(booking15)

booking16 = Booking(member13, gym_class2)
booking_repository.save(booking16)

booking17 = Booking(member14, gym_class1)
booking_repository.save(booking17)

booking18 = Booking(member15, gym_class1)
booking_repository.save(booking18)

booking19 = Booking(member16, gym_class1)
booking_repository.save(booking19)

booking20 = Booking(member17, gym_class3)
booking_repository.save(booking20)

booking21 = Booking(member18, gym_class3)
booking_repository.save(booking21)

# booking5 = Booking(member5, gym_class3)
# booking_repository.save(booking5)

select_all_classes = gym_class_repository.select_all()

# pdb.set_trace()
# print(member_repository.select_all()[0].id)
# print(member_repository.gym_classes(member1))
# print(gym_class_repository.members(gym_class1))