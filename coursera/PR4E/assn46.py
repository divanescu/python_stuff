input = raw_input("Enter Hours: ")
hours = float(input)
input = raw_input("Enter Rate: ")
rate = float(input)


def computepay():
    extra_hours = hours - 40
    extra_rate = rate * 1.5
    pay = (40 * rate) + (extra_hours * extra_rate)
    return pay


if hours <= 40:
    pay = hours * rate
    print pay
elif hours > 40:
    print computepay()
