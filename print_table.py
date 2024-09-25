table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def print_table(t):
    # find the longest string in each column and store in a list
    col_widths = [0] * len(t)
    for i in range(len(t)):
        for j in range(len(t[i])):
            if len(t[i][j]) > col_widths[i]:
                col_widths[i] = len(t[i][j])

    for i in range(len(t[0])):
        for j in range(len(t)):
            print(t[j][i].rjust(col_widths[j]) + ' ', end='')
        print('')

print_table(table_data)
