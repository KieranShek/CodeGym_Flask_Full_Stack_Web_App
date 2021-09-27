import pdb
from models.gym_class import Gym_class
from models.member import Member
from models.booking import Booking

import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
gym_class_repository.delete_all()
member_repository.delete_all()

member1 = Member('Steve', 'premium')
member_repository.save(member1)

member2 = Member('Stan', 'standard')
member_repository.save(member2)

member3 = Member('Jen', 'premium')
member_repository.save(member3)

gym_class1 = Gym_class('Spin Class', 'Cardio', '2018-07-22', '09:00', 10)
gym_class_repository.save(gym_class1)

gym_class2 = Gym_class('Leg Day', 'Strength Training', '2018-07-22', '09:00', 30)
gym_class_repository.save(gym_class2)

booking1 = Booking(member1, gym_class1)
booking_repository.save(booking1)

booking2 = Booking(member3, gym_class1)
booking_repository.save(booking2)

booking3 = Booking(member1, gym_class2)
booking_repository.save(booking3)

booking4 = Booking(member2, gym_class2)
booking_repository.save(booking4)

select_all_classes = gym_class_repository.select_all()

# pdb.set_trace()
# print(member_repository.select_all()[0].id)
# print(member_repository.gym_classes(member1))
# print(gym_class_repository.members(gym_class1))