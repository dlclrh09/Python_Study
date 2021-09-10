n = int(input())
if n % 2 != 0:
    print('Weird')
elif n in range(2, 6):
    print('Not Weird')
elif n in range(6, 21):
    print('Weird')
elif n > 20:
    print('Not Weird')


if (n % 2 != 0) | (n in range(6, 21)):
    print('Weird')
else:
    print('Not Weird')