# range1 = range(1, 5)
# list1 = list(range1)
# print(list1)
# l2 = [ n +1 for n in list1]
# print(l2)

names = ["caroline", "Elanor", "freddie"]

for i in range(len(names)):
    names[i] = names[i].upper()

print(names)