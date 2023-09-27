# Write your code here :-)
tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "elephants", "bats", "mice"],
]


def printTable(table):
    # find max value in all lists for column width
    colWidths=[0]*len(table)
    for i in range(0,len(table)):
        for j in range(0,len(table[i])):
            if len(table[i][j])>=len(tabl

    print(colWidths)

    # make table by rjust values
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colWidths[j],'+'), end=" ")
            j += 1
        print()


printTable(tableData)
