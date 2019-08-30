#0/1 Knapsack problem
def knapSack(capacity, wt, pr, n): 
    e=n-1
    f=capacity
    K = [[0 for p in range(capacity+1)] for p in range(n)] 
    print(" _p", end='')
    print(" _w_|", end='')
    for t in range(capacity+1):
        print("_",t, end='')
    print()
    for i in range(n):
        print(" ",pr[i], end='')
        print(" ",wt[i],"|", end='')
        for w in range(capacity+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i] <= w: 
                K[i][w] = max(pr[i] + K[i-1][w-wt[i]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w]
            print(" ",K[i][w], end='')
        print()
    print("The object used to add to the profit is given as 1 otherwise 0")
    x=[0 for q in range(n)]
    for g in range(1,n):
        print("x",g,"|", end='')
    print()
    while e>0 and f>0:
        if K[e][f]==K[e-1][f]:
            x[e]=0
            e=e-1
        else:
            x[e]=1
            f=f-wt[e]
            e=e-1
    for g in range(1,n):
        print(x[g],"  |", end='')
    return K[n-1][capacity]