def rotate_grid(list):
    for i in range(len(list[0])):
        for j in range(len(list)):
            print(list[j][i], end='')
        print('')


test = [['.','.','.','.','.','.'],
        ['.','O','O','.','.','.'],
        ['O','O','O','O','.','.'],
        ['O','O','O','O','O','.'],
        ['.','O','O','O','O','O'],
        ['O','O','O','O','O','.'],
        ['O','O','O','O','.','.'],
        ['.','O','O','.','.','.'],
        ['.','.','.','.','.','.']]

rotate_grid(test)
