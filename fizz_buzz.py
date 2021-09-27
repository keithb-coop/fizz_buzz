def fizz_buzz(number):
    flags = {k : number % k == 0 for k in [3,5,7]}
    if flags[3]:
        return 'Fizz'
    if flags[5]:
        return 'Buzz'
    if flags[7]:
        return 'Baz'

    return number
