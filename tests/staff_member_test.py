import unittest

from repositories.staff_member_repository import *

class TestMember(unittest.TestCase):

    def setUp(self):
        self.staff_member = Staff_Member('Steve', 'Instructor')

    def test_member_has_name(self):
        self.assertEqual("Steve", self.staff_member.name)

    def test_guest_has_membership_type(self):
        self.assertEqual('Instructor', self.staff_member.job_type)

if __name__ == '__main__':
    unittest.main()