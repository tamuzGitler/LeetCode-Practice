import math


class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fractions = []
        for numerator in range(1, n):
            for denominator in range(numerator + 1, n + 1):
                if math.gcd(numerator, denominator) == 1:
                    fractions.append(str(numerator) + "/" + str(denominator))

        return fractions


if __name__ == '__main__':
    sol = Solution()
    print(sol.simplifiedFractions(6))
