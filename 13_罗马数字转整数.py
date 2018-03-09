class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        convert_rule = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        num = 0
        word = []
        for w in s:
            word.append(w)
        i = 0
        while i < len(word):
            if i ==len(word)-1 or convert_rule[word[i]] >= convert_rule[word[i+1]]:
                num += convert_rule[word[i]]
                i += 1
            else:  
                num += (convert_rule[word[i+1]] - convert_rule[word[i]])
                i += 2
                if i > len(word)-1:
                    break
                        
        if num >= 1 and num <=3999:
            return num