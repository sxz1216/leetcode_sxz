class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        _5_rmb = []
        _10_rmb = []
        for i in bills:
            if i == 5:
                _5_rmb.append(i)
            elif i == 10:
                _10_rmb.append(i)
                try:
                    del _5_rmb[-1]
                except:
                    return False
            else:
                try:
                    del _5_rmb[-1]
                except:
                    return False
                if 10 in _10_rmb:
                    del _10_rmb[-1]
                else:
                    try:
                        del _5_rmb[-1]
                        del _5_rmb[-1]
                    except:
                        return False
                        
        return True