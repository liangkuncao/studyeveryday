class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        ddict = {1: 'One', 2: 'Two', 3: "Three", 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
                10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15:'Fifteen', 16: 'Sixteen',
                17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
                60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
        base = ['', 'Thousand', 'Million', 'Billion']
        base_i, exp = 0, 1000
        result = []
        while num:
            chunk = num % exp
            if chunk and base_i > 0:
                result.append(base[base_i])
            one = chunk % 10
            two = chunk % 100 // 10
            three = chunk // 100
            if two == 1:
                result.append(ddict[two*10 + one])
            else:
                if one:
                    result.append(ddict[one])
                if two:
                    result.append(ddict[two * 10])
            if three:
                result.append('Hundred')
                result.append(ddict[three])
            base_i += 1
            num //= exp
        return ' '.join(result[::-1])