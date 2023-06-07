class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # Create a boolean array to mark numbers as prime or not
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        # Use Sieve of Eratosthenes algorithm to mark non-prime numbers
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        # Count the number of prime numbers
        count = sum(is_prime)
        return count