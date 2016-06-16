input = raw_input("Enter Score:")
try:
    score = float(input)
except:
    print "Please use 0.0 - 1.0 range !"
    exit()
if (score < 0 or score > 1):
    print "Please use 0.0 - 1.0 range !"
elif score >= 0.9:
    print "A"
elif score >= 0.8:
    print "B"
elif score >= 0.7:
    print "C"
elif score >= 0.6:
    print "D"
else:
    print "F"

