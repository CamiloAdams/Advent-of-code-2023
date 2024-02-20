import sys
# sys.stdout = open('./input.txt', 'w')
file = open('./input.txt', 'r')
# file = open('./test.txt', 'r')
meals = file.readlines()

import re

sum1 = 0
#
# for index, line in enumerate(meals):
#     # print("Line {}: {}".format(index, line.strip()))
#     values = re.sub('[^0-9]', '', line)
#     calibration_value = values[0] + values[-1]
#     sum += int(calibration_value)
#
# print('part 1:' + str(sum))
#
## PART 2
numbers = [ 
    "zero",
    "one" ,
    "two" ,
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

sum2 = 0

def translate(line):
    for num, name in enumerate(numbers):
        line = line.replace(name, f"{name}{num}{name}")
    return line

for index, line in enumerate(meals):
    # res = [number for number in numbers if(number in line)]
    # print(res)
    #
    # dic = {}
    #
    # for number in res: 
    #     dic[numbers[number]] = line.index(number)
    #
    # values = re.sub('[^0-9]', '', line)
    # # Packet tracer v8.2.0
    # for value in values:
    #     dic[int(value)] = line.index(value) 
    # 
    # low = min(dic.values())
    # high = max(dic.values())
    #
    # low_index = [i for i in dic if(dic[i] == low)]
    # high_index = [i for i in dic if(dic[i] == high)]
    #
    # sum += low_index[0]*10 + high_index[0]
    #

    digits = [char for char in line if char.isnumeric()]
    if digits:
        sum1 += int(digits[0]+digits[-1])

    digits = [char for char in translate(line) if char.isnumeric()]
    print(int(digits[0] + digits[-1]))
    sum2 += int(digits[0] + digits[-1])
   

print(translate("two1nine"))
print(sum2)

