def computepay():
    input = raw_input("Enter Hours:")
    try:
        hours = float(input)
    except:
        print "Error, please enter a numeric input"
        exit()

    input = raw_input("Enter rate:")
    try:
        rate = float(input)
    except:
        print "Error, please enter a numeric input"
        exit()

    if hours <= 40:
        pay = hours * rate
    else:
        rate_normal = rate
        rate_extra = 1.5 * rate
        extra_hours = hours - 40
        pay = (40 * rate_normal) + (extra_hours * rate_extra)
    print "Yout get " + str(pay) + " for your " + str(hours) + " hours."
computepay()
