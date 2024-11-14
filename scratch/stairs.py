def climb_stairs(n):
    t = [0]*(n+1)
    t[0] = t[1] = 1
    for i in range(2, n+1):
        t[i] = t[i-1]+ t[i-2]
    return t[n]

if __name__=="__main__":
    print(climb_stairs(4))
