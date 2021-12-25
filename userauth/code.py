import random

number_list = [x for x in range(10)]
code = []

for i in range(5):
    numbers = random.choice(number_list)
    code.append(numbers)
print(code)
code_string = "".join(str(item) for item in code)
print(code_string)