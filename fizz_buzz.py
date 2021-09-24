def fizz_buzz(number):
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'
    if number % 7 == 0:
        return 'Baz'

    return number
