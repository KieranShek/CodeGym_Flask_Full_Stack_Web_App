import unittest

from repositories.gym_class_repository import *

class TestGym_Class(unittest.TestCase):

    def setUp(self):
        self.gym_class = Gym_class('Arm Day', 3, '2021-08-30', '12:00', 60, 12)

    def test_gym_class_has_name(self):
        self.assertEqual("Arm Day", self.gym_class.name)

    def test_guest_has_membership_type(self):
        self.assertEqual(3, self.gym_class.instructor)

    def test_gym_class_has_name(self):
        self.assertEqual('2021-08-30', self.gym_class.date)

    def test_gym_class_has_name(self):
        self.assertEqual("12:00", self.gym_class.time)

    def test_gym_class_has_name(self):
        self.assertEqual(60, self.gym_class.duration)

    def test_gym_class_has_name(self):
        self.assertEqual(12, self.gym_class.capacity)

if __name__ == '__main__':
    unittest.main()