# Numbers
a = 12
b = 5
c = 0.6
d = 17.1

print(f'a = {a} is type {type(a)}')
print(f'b = {b} is type {type(b)}')
print(f'c = {c} is type {type(c)}')
print(f'd = {d} is type {type(d)}')

print(f'a * b = {a * b} is type {type(a * b)}')
print(f'b * c = {b * c} is type {type(b * c)}')
print(f'b + c = {b + c} is type {type(b + c)}')
print(f'd - a = {d - a} is type {type(d - a)}')
print(f'a % b = {a % b} is type {type(a % b)}')
print(f'a % 5.0 = {a % 5.0} is type {type(a % 5.0)}')
print(f'b ** 2 = {b ** 2} is type {type(b ** 2)}')
print(f'a + b = {a + b} is type {type(a + b)}')
print(f'b / a = {b / a} is type {type(b / a)}')
print(f'a // b = {a // b} is type {type(a // b)}')
print(f"len('northcoders') + b = {len('northcoders') + b} is type {type(len('northcoders') + b)}")

# Strings
tutor = 'david john bartlett'
title = 'Mr'
job_title = "Senior Tutor"

shouty_name = tutor.upper()
low_key_title = title.lower()
low_key_job_title = job_title.lower()
full_honours = f"{title} {tutor.title()}, {job_title}"

# Booleans
# Returns True or False
print(f"30 > 12 is {'truthy' if 30 > 12 else 'falsy'}")
print(f"4 < 4 is {'truthy' if 4 < 4 else 'falsy'}")
print(f"12 == '12' is {'truthy' if 12 == '12' else 'falsy'}")
# True behaves as the integer 1 and False as 0
print(f"1 == True is {'truthy' if 1 == True else 'falsy'}")
print(f"0.9 < True is {'truthy' if 0.9 < True else 'falsy'}")
# and - both statements must be true
print(f"14 > 5 and len('tree') == 8/2 is {'truthy' if 14 > 5 and len('tree') == 8/2 else 'falsy'}")
# and - returns first falsy or last truthy value
print(f"3 and 4 returns {3 and 4}")
print(f"3 and 0 returns {3 and 0}")
# or - one statement must be true
print(f"3 > 4 or 5 > 2 is {'truthy' if 3 > 4 or 5 > 2 else 'falsy'}")
# or - returns first truthy value
print(f"5 or 0.7 returns {5 or 0.7}")
print(f"5 > 10 or 4 returns {5 > 10 or 4}")
# not - returns True if statement is not truthy 
print(f"not 10 > 5 is {'truthy' if not 10 > 5 else 'falsy'}")
print(f"not 10 < 5 is {'truthy' if not 10 < 5 else 'falsy'}")
print(f"not 3 is {'truthy' if not 3 else 'falsy'}")