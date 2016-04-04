# 1
"""
input_str = input('Введите строку : ')
print('Вариант 1 : ', ''.join([x for x in reversed(input_str)]))
print('Вариант 2 : ', input_str[::-1])
output_str = ''
for x in input_str:
    output_str = x + output_str
print('Вариант 3 : ',output_str)
print('Вариант 4 : ', ''.join([input_str[len(input_str)-1-x] for x in range(len(input_str))]))
"""
# 2
"""
input_str = input('Введите строку : ')
vov = 'AEUOIaeiou'
vov_count = 0
for i in input_str:
    if i in vov:
        vov_count += 1
print('Кол-во гласных : ', vov_count)
"""
# 3
"""
input_str = input('Введите строку : ')
wow_count = 0
for i,x in enumerate(input_str):
    if input_str[i:i+3] == 'wow':
        wow_count += 1
print(wow_count)
"""
# 4
"""
input_str = input('Введите строку : ')
output_str = ''
temp_str = ''
for i,x in enumerate(input_str):
    for j in range(i,len(input_str)):
        if list(input_str[i:j+1]) == list(sorted(input_str[i:j+1])):
            temp_str = input_str[i:j+1]
            if len(temp_str) > len(output_str):
                output_str = temp_str
print(output_str)
"""


# 5
def typer(data):
    print(str(type(data))[7:-1])


# 6
def analize(a, b):
    if type(a) == str or type(b) == str:
        print('Получена строка')
    elif a > b:
        print('Больше')
    elif a < b:
        print('Меньше')
    elif a == b:
        print('Равны')


# 7
def unique_ordered(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    print(b)


def unique_disordered(a):
    b = list(set(a))
    print(b)


# 8
"""
a = (1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1)
b = a[2::3]
print(b)
b = tuple(a[i] for i in range(len(a)) if i%3 == 2)
print(b)
"""
# 9
"""
x = 2
y = 2
z = 1
a = max(min(x,y), min(y,z), x)
print(a)
"""
#10
vov_letters = 'aioueAIOUE'
while True:
    vov_count = 0
    input_str = input('Введите строку (q Для выхода) : ')
    if input_str == 'q':
        break
    for x in input_str:
        if x in vov_letters:
            vov_count += 1
    print("The string contains {} vowels".format(vov_count))
print('GoodBye')