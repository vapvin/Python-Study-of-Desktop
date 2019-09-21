my_tuple2 = 'python', 'javascript', 'jQuery'
print(my_tuple2)

print('''첫 번째
두번째
세번째''')


fruit_str = 'apple banana lemon'
fruits = fruit_str.split()
print(fruits[0])

thisis = 'python'
print(thisis[:3])

my_list = [1,2,3,4,5]

for a in my_list:
    print('횟수:',a)


my_str = "cording"

for letter in my_str:
    print("문자:",letter)

for is_range in range(5):
    print("연습:",is_range)

for count2 in range(5, 10):
    print("숫자:",count2)

##곱셈 연습하기
for j in range(4):
    for i in range(3):
        print('i:{}, j:{}'.format(i,j))

for l in range(1,10):
    for m in range(1, 10):
        print('{}X{}='.format(l,m),l*m)

for two in range(1, 10):
    print('2X{}'.format(two),two*2)
##comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []
# even_numbers = []

for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)

print(odd_numbers)

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)





