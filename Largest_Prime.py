class Solution:
    def largestPrime(self, n: int) -> int:
        if n < 2:
            return 0
        prime = [True]*(n+1)
        prime[0] = prime[1] = False
        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                for j in range(i*i,n+1,i):
                    prime[j] = False
        sum = 0
        ans = 0
        for i in range(2,n+1):
            if prime[i]:
                sum+=i
                if sum > n:
                    break 
                if prime[sum]:
                    ans = sum
        return ans
