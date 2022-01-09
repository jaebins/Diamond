starLength = 15

for i in range(1, starLength, 2):
    for k in range((((starLength - i) // 2) * 2) + 1):
        if(k == (starLength - i) // 2):
            for j in range(i):
                print('*', end="")
        else:
            if(k == 0 or k == (((starLength - i) // 2) * 2)):
                print('I', end="")
            else:
                print('-', end="")
    print("")

for i in range(starLength - 2, -1, -2):
    for k in range((((starLength - i) // 2) * 2) + 1):
        if(k == (starLength - i) // 2):
            for j in range(i):
                print('*', end="")
        else:
            if(k == 0 or k == (((starLength - i) // 2) * 2)):
                print('I', end="")
            else:
                print('-', end="")
    print("")
