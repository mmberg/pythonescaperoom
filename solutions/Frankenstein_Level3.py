import random

def run():

    def unique_digits(a):

        digits = [int(i) for i in str(a)]

        if digits[0] == digits[1]:
            return False
        
        elif digits[0] == digits[2]:
            return False

        elif digits[1] == digits[0]:
            return False

        else:
            return True

    def cross_sum(a):

        cross_sum_digits = [int(i) for i in str(a)]

        return sum(cross_sum_digits)

    numbers = []

    while len(numbers) < 3:

        x = random.randint(101,998)

        if unique_digits(x) == True:

            if cross_sum(x) >= 9 and cross_sum(x) <= 15:

                numbers.append(x)

        else:
            continue

    badge_number = '-'.join(map(str, numbers))
    
    print(badge_number)
    return badge_number