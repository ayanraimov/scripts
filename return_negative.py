def make_negative( number ):
    if number == 0:
        return 0
    elif number * 1 < 0:
        return number
    elif number * 1 > 0:
        number = number * -1
        return number
    pass

make_negative(-3)
make_negative(0)
make_negative(7)
