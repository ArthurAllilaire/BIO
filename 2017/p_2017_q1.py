def colors_add(c1, c2):
    if c1 == c2:
        return c2 #Same color
    colors = ['R','G','B']
    colors.remove(c1)
    colors.remove(c2)
    return colors[0]

def final_colour(start):
    while len(start) > 1:
        next = []
        for i in range(len(start)-1):
            next.append(colors_add(start[i], start[i+1]))
        start = next
        # print(start)

    return start[0]
        
#1A - this is too easy for BIO imo
#print(final_colour("RRGBRGBB"))

#1B - I cba to think icel
#RRGBRGBB - okay i've decided to think
#So first two have to be RR OR GBG - then 
def before(row, results, curr=""):
    if len(row) == 0:
        results.add(curr)
        return results
    colors = ['R','G', 'B']
    if curr:
        char, row = row[0], row[1:]
        char2 = curr[-1]
        if char == char2:
            return before(row, results, curr+char)
        else:
            colors.remove(char)
            colors.remove(char2)
            return before(row, results, curr+colors[0])
    else:
        for c in colors:
            results.update(before(row, results, c))
        return results

#1B - I got the computer to do it :)
#{'GBGGRRBBB', 'RRRBBGGRG', 'BGBRGBRGR'}
#print(before('RRGBRGBB', set()))

#1C - only 1 way - know end one + 1 above, so can figure out the ones to either side and so on

#1D - RBGR -> GRB -> BG -> R
# RRRR -> RRR -> RR -> R
def get_RGB(counts):
    colors = ['R','G','B']
    result = []
    for i in counts:
        result.append(colors[i])
    return "".join(result)

def update_counts(counters):
    """Returns False if reached the end otherwise increments by 1"""
    if len(counters) == 0: # Reached the end
        return False
    counters[-1] += 1
    if counters[-1] == 3:
        counters.pop()
        new_counts = update_counts(counters)
        if new_counts:
            new_counts.append(0)
            return new_counts
    return counters
update_counts([0,2])
def get_perms(n):
    counters = [0]*n
    while counters:
        yield get_RGB(counters)
        counters = update_counts(counters)
        if counters == False:
            break

#Just gonna brute force it as usual
def same(n):
    #Need all permutations
    for comb in get_perms(n-2):
        if final_colour('R'+comb+'R') != 'R':
            return False
    return True

#1D -> 4,10
# Outputs 4,10 and the rest takes too long 3**28 is a big number tbf (why is it 3**k+1)
# for i in range(4,30):
#     if same(i):
#         print(i)
