# OEFENING 1
# lijst1 = [1, 2, 3, 10]
# lijst2 = [4, 5, 6]
# eindlijst = []

# max_length = min(len(lijst1), len(lijst2))
# etc_length = max(len(lijst1), len(lijst2))

# if len(lijst1) > len(lijst2):
#     max_lijst = lijst1
# elif len(lijst2) > len(lijst1):
#     max_lijst = lijst2

# for i in range(max_length):
#     eindlijst.append(lijst1[i] + lijst2[i])

# for j in range(max_length, etc_length):
#     eindlijst.append(max_lijst[j])

# print(eindlijst)

# OEFENING 2
# for i in range(5):
#     for j in range(i):
#         print("*", end=" ")
#     print("")
# for i in range(-5, 0):
#     for j in range(abs(i)):
#         print("*", end=" ")
#     print("")


# OEFENING 3

# getal1 = int(input())
# getal2 = int(input())
# getal3 = int(input())

# eindlijst = [[getal1 for i in range(3)], [getal2 for i in range(3)], [getal3 for i in range(3)]]

# print(eindlijst)

# OEFENING 4

# array = [[1, 0, 1, 1, 0], [0, "x", "x", 0, 0], [1, 0, 1, 1, "x"],[0, "x", 0, 1, 1]]

# eindlijst = []

# for i in range(1, len(array)):
#     for j in range(len(array[i])-1):
#         if array[i][j] == "x" and array[i-1][j+1] == 1:
#             eindlijst.append((i,j))

# print(eindlijst)