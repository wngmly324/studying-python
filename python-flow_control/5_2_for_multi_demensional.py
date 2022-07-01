persons = [
    ['egoing','Seoul','Web'],
    ['basta','Seoul','IOT'],
    ['blackdew','Tongyeong','ML']
]
print(persons[0][0])

for person in persons:
    print(person[0] + ', ' + person[1] + ', ' + person[2])

person = ['egoing','Seoul','Web']
name = person[0]
address = person[1]
interest = person[2]
print(name, address, interest)

name, address, interest = ['egoing','Seoul','Web']
print(name, address, interest)

for name, address, interest in persons:
    print(name + ', ' + address + ', ' + interest)

# 출처
# 생활코딩, "Python 제어문 - 5.2. 반복문 - 다차원배열의 처리", https://www.youtube.com/watch?v=xcz1WwPm1kM
