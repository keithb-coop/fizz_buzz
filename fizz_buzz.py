from collections import defaultdict


def fizz_buzz(number):
    justANumber = JustANumber()
    baz = StringANumber(7, "Baz", justANumber)
    bar = StringANumber(5, "Buzz", baz)
    fizz = StringANumber(3, "Fizz", bar)

    return fizz.stringThis(number, "")


class StringANumber:
    def __init__(self, mulitpleOf=None, stringToUse=None, next=None):
        self.multipleOf = mulitpleOf
        self.stringToUse = stringToUse
        self.next = next

    def stringThis(self, number, stringSoFar):
        handlers = {1: (lambda n: self.next.stringThis(n, stringSoFar)),
                    self.multipleOf: (lambda n: self.next.stringThis(n, stringSoFar + self.stringToUse))}

        divisors = [ n for n in [1, self.multipleOf] if number % n == 0]
        return handlers[max(divisors)](number)


class JustANumber():
    def __init__(self):
        self.handlers = defaultdict(lambda: (lambda n, stringSoFar: stringSoFar),
                                    {0: (lambda n, stringSoFar: str(n))})

    def stringThis(self, number, stringSoFar):
        return self.handlers[len(stringSoFar)](number, stringSoFar)
