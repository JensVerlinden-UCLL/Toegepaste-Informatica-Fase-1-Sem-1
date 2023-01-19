# OEFENING 1
# a = "5"
# b = 3

# print("I want ", a, "puppies and " + b, "kats!") 

# OEFENING 2
# print(f"{(41+200) % 24}:00")

# OEFENING 3
# a = input("Give number: ")
# print(a)

# OEFENING 4
# def exercise4():
#     a = input("Whats your firstname? ")
#     b = int(input("Whats your age? "))
#     print(a + b)

# exercise4()

# OEFENING 5
# def exercise5():
#     amount = 99
#     a = amount // 15
#     b = amount % 15
#     c = a // 3
#     d = b % 3
#     print(a, b, c, d)

# exercise5()

# OEFENING 6
# def exercise6():
#     answer = input('Enter a string: ')
#     print(len(answer))

# exercise6()

# OEFENING 7
# def exercise7():
#     score = int(input())
#     if score <= 30:
#         letter_grade = 'Max score'
#     elif score >= 15:
#         letter_grade = 'You just passed'
#     else:
#         letter_grade = 'Failed!'
#     print(letter_grade)

# exercise7()

# OEFENING 8
# def exercise8():
#     number = int(input())
#     if number == 10:
#         print("A")
#     if number < 30:
#         print("B")
#     if number > 5:
#         print("C")
#     if number < 11:
#         print("D")
#     if number < 4:
#         print("E")

# exercise8()

# OEFENING 9
# def exercise9():
#     a = True
#     b = False
#     c = False
#     if a or b and c: 
#         print("A")
#     else:
#         print("B")
    
# exercise9()

# OEFENING 10
# def exercise10():
#     a = True
#     b = False
#     c = False

#     if not a or b:
#         print(1)
#     elif not a or not b and c:
#         print(2)
#     elif not a or b or not b and a:
#         print(3)
#     else:
#         print(4)

# exercise10()


# OEFENING 11
# def exercise11():
#     count = 1
#     for i in range(3):
#         count += 1
#     print(count)

# exercise11()

# OEFENING 12
# def exercise12():
#     for i in range(3, 10):
#         j = i + 2
#         print(j)

# exercise12()

# OEFENING 13
# def exercise13():
#     a = int(input())
#     b = int(input())
#     total = 0
#     while (a<=b):
#         total += a
#         a += 1
#     print(total)

# exercise13()

# OEFENING 14
# def exercise14():
#     array = [1, 6.0, "9", 1.34, 32]
#     for i in array:
#         if isinstance(i, int):
#             print(i)

# exercise14()

# OEFENING 15
# def exercise15():
#     a = []
#     for i in range(5):
#         a.append(i)

#     b = []
#     for i in range(7):
#         if i in a and i%2 == 0:
#             b.append(i)
#     print(b)

# exercise15()

# OEFENING 16
# def exercise16():
#     temp = ['Geeks', 'for', 'Geeks']
#     array = []
#     for i in temp:
#         array.append(i[0].upper())
#     print(array)

# exercise16()

# OEFENING 17
# def exercise17():
#     n=5
#     for i in range(n):
#         for j in range(i):
#             print('* ', end='')
#         print('')

#     for i in range(n, 0, -1):
#         for j in range(i):
#             print('* ', end='')
#         print('')

# exercise17() 

# OEFENING 18
# def exercise18():
#     array = []
#     for i in range(3):
#         sArray = []
#         for k in range(3):
#             sArray.append(i)

#         array.append(sArray)

#     print(array)

# exercise18()

# OEFENING 19
# def exercise19(array2D, getal):
#     for i in array2D:
#         for k in i:
#             if k % getal == 0:
#                 print(k)
# exercise19([[1,3,4],[12,9,45]], 3)
            
# OEFENING 20
# def exercise20(b):
#     newArray = []
#     for i in b:
#         sArray = []
#         for k in i:
#             if k != 10:
#                 sArray.append(k)
#         newArray.append(sArray)
    
#     print(newArray)

# a = [[1,2,4,58],[3,10, 5, 12],[3, 4, 10, 52]]
# exercise20(a)

# print(sum([1,5,7], 10))