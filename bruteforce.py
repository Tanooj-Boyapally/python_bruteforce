from itertools import permutations

list_hints = input("enter list of names: ")
name_list = list_hints.split()
file = open("demofile.txt", "w")
for j in range(1, len(name_list) + 1):
    for i in permutations(name_list, j):
        file.write(''.join(i) + '\n')