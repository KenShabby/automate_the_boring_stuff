# Implement the Collatz Squence

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return(3 * number + 1)
    
print('Enter a number: ', end='')
response = int(input())

while(response != 1):
    response = collatz(response)
