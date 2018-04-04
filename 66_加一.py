class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        number = 0
        for k,v in enumerate(digits):
            number += int(v)*10**(length-1-k)
        number += 1 
        new_length = len(str(number))
        d = []
        for i in str(number):
            d.append(int(i))

        return d
