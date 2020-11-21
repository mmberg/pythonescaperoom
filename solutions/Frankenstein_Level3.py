def create_badge_number():
    '''
    create a badge number with format xxx-xxx-xxx
    requirements per block of 3: cross sum is between 9 and 15, the digits are digits
    '''

    def unique_digits(a):                                       # function to check uniqueness of digits in a number

        digits = [int(i) for i in str(a)]

        if digits[0] == digits[1]:
            return False
        
        elif digits[0] == digits[2]:
            return False

        elif digits[1] == digits[0]:
            return False

        else:
            return True

    def cross_sum(a):                                           # function to calculate the cross sum

        cross_sum_digits = [int(i) for i in str(a)]

        return sum(cross_sum_digits)

    numbers = []                                              # list of three digit numbers for the badge number

    import random

    while len(numbers) < 3:                                  # while we have less than 3 items in the list

        x = random.randint(101,998)                             # get random 3 digit number

        if unique_digits(x) == True:                            # check if all digits are unique

            if cross_sum(x) >= 9 and cross_sum(x) <= 15:        # check if cross sum is 9

                numbers.append(x)                             # add number to ints list

        else:
            continue

    badge_number = '-'.join(map(str, numbers))
    
    print(badge_number)
    return badge_number

create_badge_number()