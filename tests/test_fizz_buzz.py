from fizz_buzz import FizzBuzzer
from unittest import TestCase

class TestFizzBuzzer(TestCase):

    def TestFizz(self):
        buzzer = FizzBuzzer(11)
        self.assertEqual(buzzer.start, 11)
        self.assertEqual(buzzer.number, 11)
        self.assertIsInstance(buzzer, FizzBuzzer)
        self.assertEqual(buzzer.next(), "fizz")
        self.assertEqual(buzzer.next(), 13)
        buzzer.next()
        self.assertEqual(buzzer.next(), "fizzbuzz")
        buzzer = FizzBuzzer()
        self.assertEqual(buzzer.start, 0)

        


