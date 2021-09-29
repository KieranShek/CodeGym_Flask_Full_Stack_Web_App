import unittest

from repositories.member_repository import *

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member = Member('Jack', 'Premium')

    def test_member_has_name(self):
        self.assertEqual("Jack", self.member.name)

    def test_guest_has_membership_type(self):
        self.assertEqual('Premium', self.member.type)

if __name__ == '__main__':
    unittest.main()