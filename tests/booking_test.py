import unittest

from repositories.booking_repository import *
from repositories.member_repository import *
from repositories.gym_class_repository import *
from repositories.staff_member_repository import *

class TestMember(unittest.TestCase):

    def setUp(self):
        member1 = Member('Jack', 'Premium')
        gym_class1 = Gym_class('Spin Class', 1, '2021-09-01', '09:00', 45, 10)
        self.booking = Booking(member1, gym_class1)

    def test_booking_has_name(self):
        self.assertEqual("Spin Class", self.booking.gym_class.name)

    def test_booking_has_instructor(self):
        self.assertEqual(1, self.booking.gym_class.instructor)

    def test_booking_has_member(self):
        self.assertEqual("Jack", self.booking.member.name)

    def test_booking_has_name(self):
        self.assertEqual("Premium", self.booking.member.type)




if __name__ == '__main__':
    unittest.main()