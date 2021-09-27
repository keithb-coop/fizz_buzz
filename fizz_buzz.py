def fizz_buzz(number):
    divisors = filter(lambda k: number % k == 0, [1,3,5,7])
    printers = {1: (lambda n: n),
                3: (lambda n: "Fizz"),
                5: (lambda n: "Buzz"),
                7: (lambda n: "Baz")}

    return printers[max(divisors)](number)
