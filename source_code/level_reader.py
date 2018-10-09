file = open("level1.txt","r")
rows = file.readlines()
file.close()

layout = [[0]*24]*24
row_num = 0

for row in rows:
    for index in range(len(row)):
        layout[row_num][index] = row[index]
    row_num+=1


print(layout)
