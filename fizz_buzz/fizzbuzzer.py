#create class FizzBuzzer
class FizzBuzzer:
    #attributs:
    #   start = 0
    #   number = start
    def __init__(self, start = 0):
        self.start = start
        self.number = self.start

    #methode => next
    def next(self):
        """
            return 'fizz' if start is evenly divisible by 3
            return  'buzz' if start is evenly divisible by 5
            return 'fizzbuzz' if start is evenly divisible by 3 and 5
            else the fizzbuzz value is the value of n converted into a strin

        """
        self.start += 1
        if (self.start % 3 ==0) and (self.start % 5 ==0):
            return "fizzbuzz"
        elif (self.start%3==0):
            return "fizz"
        elif (self.start%5==0):
            return "buzz"
        else:
            return str(self.start)

