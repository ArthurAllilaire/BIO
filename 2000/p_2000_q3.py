def generateDice(d1, d2):
    import itertools
    #Okay looking at this need to have at least 1 1 in each
    result = {}
    for i in d1:
        for j in d2:
            i,j = int(i), int(j)
            sum = i+j
            if sum in result:
                result[sum] += 1
            else:
                result[sum] = 1

    
    print(result)
    needed = []
    for sum, tally in result.items():
        #Therefore needs to have 5 of 7,6,5,4,3,2,1 and their pair on each one
        pos = []
        for i in range(1,sum):
            pos.append((i, sum-i))
        #For each one shows that we need
        needed.append((pos, tally))
        #Need to start with shortest ones
        needed = sorted(needed, key=lambda x:len(x[0]))
    dice = ([],[])
    print(needed)
    while needed:
        pairs, tally = needed.pop(0)
        for pos in itertools.combinations_with_replacement(pairs, tally):
            for pair in pos:
                new_dice = dice
                new_dice[0].append(pair[0])
                new_dice[1].append(pair[1])
            if dice_valid(dice):
                dice_deeper(new_dice, needed)

            print(pos)
            #For each one need to create a recursive function that adds it to the dice, then checks if it is valid with current output then continues to see if it works with the next pairs if falis move onto next one



    # import itertools

    # for d1 in itertools.combinations_with_replacement('123456',6):
    #     for d2
    # pass

generateDice("241356", "642315")