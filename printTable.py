# Write your code here :-)
tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "bats", "mice"],
]


def printTable(table):
    # find max value in all lists for column width
    colWidths=[0]*len(table)
    for x in range(len(table)):
        for y in table[x]:
            if colWidths[x]<len(y):
                colWidths[x]=len(y)



    # make table by rjust values
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colWidths[j]), end=" ")
            j += 1
        print()


printTable(tableData)
