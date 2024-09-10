import unittest

import our_functions

# yyyy-mm-dd

class test_is_valid_date(unittest.TestCase):
    def test_correct_date_month_year_format(self):
        date_str = "2023-01-01"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, True)

    def test_incorrect_date_format(self):
        date_str = "03-12-2023"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)
    
    def test_incorrect_null(self):
        date_str = ""
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_incorrect_overleny(self):
        date_str = "20231-12-31"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_incorrect_lessleny(self):
        date_str = "999-12-13"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_incorrect_overm(self):
        date_str = "2021-13-03"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)
    
    def test_incorrect_leapy2(self):
        date_str = "2000-02-29"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, True)

    def test_incorrect_noleapy(self):
        date_str = "vfdv-vf-de"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test2(self):
        date_str = "2020-11-31"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    # chat

    def test_non_leap_year(self):
        date_str = "2019-02-29"  # 2019 is not a leap year
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)  # Invalid non-leap year date


class test_is_valid_username(unittest.TestCase):
    def test_username_more_than_min(self):
        username_str = "myname"
        min_username_chars = 5
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, True)

    def test_username_equal_min(self):
        username_str = "myname"
        min_username_chars = 6
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, True)

    def test_username_2(self):
        username_str = "us"
        min_username_chars = 3
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)

    def test_username_3(self):
        username_str = "ABC"
        min_username_chars = 3
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)

    def test_username_4(self):
        username_str = "123"
        min_username_chars = 3
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)
    
    # chat
    def test_username_type_error(self):
        with self.assertRaises(TypeError):
            our_functions.is_valid_username(12345, 3)  # Non-string username

    def test_minlen_value_error(self):
        with self.assertRaises(ValueError):
            our_functions.is_valid_username("validname", 0)  # minlen < 1

# if __name__ == "__main__":
#     unittest.main()