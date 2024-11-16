import unittest

from social_age import get_social_status


class TestSocialAge(unittest.TestCase):

    def test_can_get_child_status(self):
        age = 8
        expect_res = 'ребенок'
        function_res = get_social_status(age)
        self.assertEqual(expect_res, function_res)

    def test_can_get_teen_status(self):
        age = 17
        expect_res = 'подросток'
        function_res = get_social_status(age)
        self.assertEqual(expect_res, function_res)

    def test_can_get_adual_status(self):
        age = 33
        expect_res = 'взрослый'
        function_res = get_social_status(age)
        self.assertEqual(expect_res, function_res)

    def test_can_get_eged_status(self):
        age = 60
        expect_res = 'пожилой'
        function_res = get_social_status(age)
        self.assertEqual(expect_res, function_res)

    def test_can_get_gaffer_status(self):
        age = 70
        expect_res = 'пенсионер'
        function_res = get_social_status(age)
        self.assertEqual(expect_res, function_res)

    def test_cannot_pass_str_as_age(self):
        age = 'old'
        with self.assertRaises(ValueError):
            get_social_status(age)

    def test_negative_age(self):
        age = -5
        with self.assertRaises(ValueError):
            get_social_status(age)
            
