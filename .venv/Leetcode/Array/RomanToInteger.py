class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        for i in range(len(s) - 1):
            temp = s[i] + s[i + 1]
            noEntry = s[i - 1] + s[i]
            string = s[i]
            if temp in roman.keys():
                sum = sum + roman[temp]
            elif noEntry in roman.keys():
                continue
            else:
                sum = sum + roman[string]

        return (sum)

if __name__ == "__main__":

    S = Solution()
    print(S.romanToInt('MCMXCIV'))