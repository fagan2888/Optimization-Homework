with open("./coins.dat", 'r') as f:
    x = f.readlines()
m = int(x[0].strip())
k = int(x[1].strip())
coins = [int(i) for i in x[2].strip().split(" ")]


def minCoin(m, k, coins):
    ans = [float("inf")] + [float("inf")] * len(range(1, max(coins) * k + 1))
    
    for i in range(1, max(coins) * k + 1):
        
        for c in sorted(coins, reverse=True):
            if c > i:
                continue
                
            if i == c:
                ans[i] = 1
            
            if ans[i - c] + 1 < ans[i]:
                ans[i] = ans[i - c] + 1
            
    return ans

if __name__ == "__main__":
    ans = minCoin(m, k, coins)
    for ind, n in enumerate(ans):
        if n > k and ind > 0:
            print("the smallest value: ", ind)
            break

'''
the smallest value:  1509
'''