import unittest

from shared.week_38_oop import Person


class TestPerson(unittest.TestCase):
    def test_create_person(self):
        person = Person("zaid", 30, "zaid@example.com")
        self.assertEqual(person.name, "zaid")
        self.assertEqual(person.age, 30)
        self.assertEqual(person.email, "zaid@example.com")
        self.assertNotEqual(person.name, "danny")
        self.assertNotEqual(person.age, 45)
        self.assertNotEqual(person.email, "danny@example.com")

    def test_invalid_name_arg(self):
        person = Person("zaid", 30, "zaid@example.com")
        with self.assertRaises(ValueError):
            person.name = True
            person.name = 30

    def test_invalid_age_arg(self):
        person = Person("zaid", 30, "zaid@example.com")
        with self.assertRaises(ValueError):
            person.age = -125
            person.age = 0
            person.age = 125

    def test_invalid_email_arg(self):
        person = Person("zaid", 30, "zaid@example.com")
        with self.assertRaises(ValueError):
            person.email = "zaid_example.com"


if __name__ == "__main__":
    unittest.main()
