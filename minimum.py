list = [54, 53, 77, 83, 409]

min = list[0]
for i in list:
    for j in list:
        if j < min:
            min = j

min2 = list[0]
for i in list:
    if i < min2:
        min2 = i
print(min2)

