
def justify(words, max_width=16):
    lines = [[]] # [ [ 'word', 'word' ] ]

    cli = 0 # current line index
    cll = 0 # current line total word length

    for word in words:
        if (cll + (len(lines[cli]) - 1) + len(word)) >= max_width:
            n_words = len(lines[cli])
            spaces_needed = max_width - (cll + n_words - 1)
            gaps = n_words - 1
            if gaps == 0:
                print('no gaps!')
                lines[cli][0] += ' '*spaces_needed
            else:

                even_spaces = spaces_needed // gaps
                rema_spaces = spaces_needed % gaps

                for i in range(n_words-1):
                    lines[cli][i] += ' '*(even_spaces+1)
                for i in range(rema_spaces):
                    lines[cli][i] += ' '

            lines[cli] = ''.join(lines[cli])

            lines.append([word])
            cli += 1
            cll = len(word)
        else:
            lines[cli].append(word)
            cll += len(word) # ignore spaces until check
    lines[-1] = ' '.join(lines[-1])
    final_spaces = max_width - (len(lines[-1]))
    lines[-1] = lines[-1] + ' '*final_spaces
    justified = lines
    return justified


# accumulative algorithm (total water captured by histogram-flavoured input)
def trap(heights):
    left_walls = []
    b = 0 # calculated volume h
    v = 0 # total volume
    for i in range(1, len(heights)):
        h = heights[i]
        p = heights[i-1]
        if h < p: # going down
            left_walls.append((i-1,p)) # add previous as left wall
            b=h
        elif p < h: # going up
            if not left_walls:
                continue
            while left_walls and b<min(h,left_walls[-1][1]):
                li, lh = left_walls[-1] # values at top of the stack
                th = min(h, lh)-b # top of the area to calulate (b is bottom)
                tw = i-li-1 # width of area to calculate
                v+=th*tw
                b=min(h,lh)
                # if min(h,lh) == lh:
                if lh <= h:
                    left_walls.pop()
                # if min(h, lh) == h:
    return v


def enoughGasForCircuit(gas, cost):
    """
    because of forward-backward guarantee, if we have more or as much gas as
    cost, there exists a solution.
    """

    # early return if not enough gas
    if sum(gas) < sum(cost):
        return -1

    # tank has no gas, starting as first gas station
    t = 0
    s = 0

    for i in range(len(gas)):
        t += gas[i] - cost[i]

        if t < 0:
            s = i+1
            t=0

    return s


def jump(nums):
    """
    the insight here is that we want to work backwards through the options and
    select the minimum from the list of options. It is somewhat inefficient as
    we concatenate the jump range.
    Like the knapsack problem we work backwards from the "full" configuration;
    top of the stair, desired state.
    """

    sol = [float('inf')]*len(nums)
    sol[-1] = 0
    min_jumps = float('inf')
    closest = len(nums)-1
    for i in range(len(nums)-2, -1, -1):
        if nums[i] > 0:
            k = sol[i+1:min(len(nums)+1, i+nums[i]+1)]
            closest = min(k)
            sol[i] = closest+1

    return sol[0]


def rotate(arr, k):
    """
    Easiest to just do three reversals
    """
    n = len(arr)
    if n == 1:
        return
    if k == 0 or k == len(arr):
        return
    def reverse(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1

    a = k if k < n else k % n
    reverse(0, n-1)
    reverse(0, a-1)
    reverse(a, n-1)

def candy(ratings):
    """
    Minimum candy to distribute amongst children, who are rated. Higher rated
    kids must have more candy than those beside them. Kids need at least
    1 candy each.
    """
    candy = [1]*len(ratings)
    for i in range(1, len(candy)):
        # if decreasing from previous, do nothing, keep 1
        # if increasing from previous, current = previous candy + 1
        if ratings[i] < ratings[i-1]:
            if candy[i] == candy[i-1]:
                candy[i-1] = candy[i]+1
        if ratings[i] > ratings[i-1]:
            candy[i] = candy[i-1]+1
    for i in range(len(candy)-2, -1, -1):
        if ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
            candy[i] = candy[i+1]+1
    return sum(candy)

if __name__=="__main__":
    # justified = justify(["This", "is", "an", "example", "of", "text", "justification."])
    # for line in justified:
    #     print(line)

    trapped = trap([0,1,0,2,1,0,1,3,2,1,2,1])
    arr = [1, 2, 3, 4, 5, 6]
    rotate(arr, 2)
    # print(trapped) # expected 6
