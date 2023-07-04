class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 0
        prime = [True for i in range(n)]
        p = 2
        prime_count = 0
        while (p * p < n):

            # If prime[p] is not
            # changed, then it is a prime
            if (prime[p] == True):

            # Update all multiples of p
                for i in range(p * p, n, p):
                    prime[i] = False
            p += 1

        # Print all prime numbers
        for p in range(2, n):
            if prime[p]:
                prime_count += 1
        return prime_count

obj = Solution()
print(obj.countPrimes(100))