#Make evaluate multiple conditions
#  or = at least one condition must be True
# and = both condition must be True
# not = invert the condition, (not False, not True)

temp = 20

is_sunny = True

if temp >= 28 and is_sunny:
    print('It is hot outside')
    print('It is sunny')
elif temp <=0 and is_sunny:
    print('It is cold outside')
    print('It is sunny')
elif 28 > temp > 0 and is_sunny:
    print('It is warm outside')
    print('It is sunny')
elif 28 > temp > 0 and not is_sunny:
    print('It is warm outside')
    print('It is cloudy')