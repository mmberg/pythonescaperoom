import random

name = 'Adam Chattoway'

def run(name):

    # Slicing & Indexing to get the initials from the name

    def get_initials(name):

        initials =[]
        names = name.split()

        for i in range(0,2):
            initials.append(names[i][0])

        return initials

    # Using the initials for the seed

    initials = get_initials(name)

    def create_seed(initials):

        seed_digits = [ord(i) for i in str(initials)]

        return sum(seed_digits)

    seed = create_seed(initials)

    # Check if the digits are unique within a 3 digit block

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

    # Calculate a cross sum for a given number

    def cross_sum(a):

        cross_sum_digits = [int(i) for i in str(a)]

        return sum(cross_sum_digits)

    # Randomly create 3-digit numbers from seed, check the requirements and add to list if they are met

    random.seed(seed)

    numbers = []

    while len(numbers) < 3:

        x = random.randint(seed,988)

        if unique_digits(x) == True:

            if cross_sum(x) >= 9 and cross_sum(x) <= 15:

                numbers.append(x)

        else:
            continue

    # Create the strings and join/add everything together
    
    badge_initials = ''.join(get_initials(name))
    badge_nums = '-'.join(map(str, numbers))

    badge_number = badge_initials + '-' + badge_nums
    
    print(badge_number)
    return badge_number

run(name)