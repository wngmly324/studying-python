person = {'name':'egoing','address':'Seoul','interest':'Web'}
print(person['name'])

for key in person:
    print(key, person[key])

persons = [
    {'name':'egoing','address':'Seoul','interest':'Web'},
    {'name':'basta','address':'Seoul','interest':'IOT'},
    {'name':'blackdew','address':'Tongyeong','interest':'ML'}
]

print('=== persons ===')

for person in persons:
    for key in person:
        print(key, ':', person[key])
    print('----------------')
    
    
# 출처
# 생활코딩, "Python 제어문 - 5.3. 반복문 - Dictionary", https://www.youtube.com/watch?v=QBsXqzM4CQM
