def is_stressful(string):
    import re

    if string.upper() == string:
        return True

    elif re.search(r'h+.*e+.*l+.*p+.*', string, re.I):
        return True

    elif re.search(r'a+.*s+.*a+.*p+.*', string, re.I):
        return True

    elif re.search(r'u+.*r+.*g+.*e+.*n+.*t+.*', string, re.I):
        return True

    elif re.search(r'!!!$', string):
        return True

    else:
        return False

print(is_stressful("Hi"))
print(is_stressful("I neeed HELP"))
print(is_stressful("something is gona happen"))
print(is_stressful("I\u2019m REALLY happy on my vacation!"))
print(is_stressful("Heeeeeey!!! I\u2019m having so much fun!\u201d"))
