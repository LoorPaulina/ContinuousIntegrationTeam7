"""Unit testing """
import unittest
from main import GymMembership

class TestGymMembership(unittest.TestCase):
    """ Test """

    def setUp(self):
        """ Test """
        self.membership = GymMembership()

    def test_select_membership_plan_valid(self):
        """ Test Select Membership Valid """
        self.membership.select_membership_plan('Basic', 1)
        self.assertEqual(self.membership.selected_plan, 'Basic')
        self.assertEqual(self.membership.num_members, 1)

    def test_select_membership_plan_invalid(self):
        """ Test Select Membership Invalid """
        with self.assertRaises(ValueError):
            self.membership.select_membership_plan('InvalidPlan', 1)

    def test_add_additional_features_valid(self):
        """ Test Additional Features Valid """
        self.membership.select_membership_plan('Premium', 1)
        self.membership.add_additional_features(['Personal Training', 'Group Classes'])
        self.assertEqual(self.membership.selected_features, ['Personal Training', 'Group Classes'])

    def test_add_additional_features_invalid(self):
        """ Test Additional Features Invalid """
        with self.assertRaises(ValueError):
            self.membership.add_additional_features(['Invalid Feature'])

    def test_calculate_cost_basic_plan(self):
        """ Test Calculate Cost Basic Plan Valid """
        self.membership.select_membership_plan('Basic', 1)
        self.assertEqual(self.membership.calculate_cost(), 50)


if __name__ == '__main__':
    unittest.main()
    