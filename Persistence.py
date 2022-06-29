def persistance(num):
    persistence = 1
    product = 1
    for digit in str(num):
        product *= int(digit)
    if len(str(num)) == 1:
        return 0
    while len(str(product)) != 1:
        old_product = product
        product = 1
        for digit in str(old_product):
            product *= int(digit)
        persistence += 1
    return persistence

persistence = 1
choice = input('Do you want to find the persistence of a certain number(y/n)?')
if choice == 'y':
    try:
        input_num = int(input('Enter the number which is wanted'))
        persistence = persistence(input_num)
        print('Persistence of ' + str(input_num) + ' is ' + str(persistence))
    except TypeError:
        print('The entered value is not a number')
else:
    print('Checking for smallest numbers of persistence. Press Ctrl + C to stop')
    max_pers = 2
    for num in range(26, 10000000):
        z = True
        for counter in range(len(str(num))):
            if str(num)[counter - 1] >= str(num)[counter]:
                z = False
                break
        if z == True:
            continue
        if '2' in str(num) and '3' in str(num) or '2' in str(num) and '4' in str(num) or '1' in str(num):
            continue
        if str(num).count('2') > 1:
            continue
        persistence = persistance(num)
        if max_pers < persistence:
            print('The smallest number with persistence ' + str(persistence) + ' is ' + str(num))
            max_pers = persistence
