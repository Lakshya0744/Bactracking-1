# Time Complexity : O(3^n)
# Space Complexity : O(3^n)

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result = []
        def recur(num, target, expr, prev, curr, index):
            if index==len(num):
                if curr == target:
                    result.append(expr)
                return
            for i in range(index, len(num)):
                #preceeding zeros
                if(index!=i and num[index]=='0'):
                    break
                
                elem = int(num[index:i+1])
                
                if index==0:
                    recur(num, target, expr+str(elem), elem,curr + elem, i+1)
                else:
                    #+
                    recur(num, target, expr + "+" + str(elem), elem, curr+elem, i+1)
                    #-
                    recur(num, target, expr + "-" + str(elem), -elem, curr-elem, i+1)
                    #*
                    recur(num, target, expr + '*' + str(elem), prev*elem, curr - prev+ prev*elem, i+1)
                    

        recur(num, target, '', 0, 0, 0)
        return result