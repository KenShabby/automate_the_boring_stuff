spam = ['apples', 'bananas', 'tofu', 'cats']

def oxford(list):
    for i in range(len(list)-1):
        print(list[i] + ', ', end='')
    print('and ' + list[-1])

oxford(spam)
