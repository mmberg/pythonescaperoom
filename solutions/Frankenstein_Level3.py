def create_badge_number():
    '''
    format xxx-xxx-xxx
    requirements per block of 3: cross sum is 9, unique digits
    '''

    def cross_sum(a):

        return 9

    ints = []

    import random

    for i in range(0,3):

        x = random.randint(101,998)

        if cross_sum(x) == 9:

            ints.append(x)

    #check requirements

    #badgeNumber = '-'.join(blocks)

    return(ints)

print(create_badge_number())