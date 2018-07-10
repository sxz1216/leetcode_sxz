class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        elif A == B:
            same = set()
            for i in A:
                if i in same:
                    return True
                same.add(i)
            return False
        else:
            pairs = []
            for a,b in itertools.izip(A,B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) >= 3:
                    return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]