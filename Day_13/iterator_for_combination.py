'''
Iterative approach
'''

class CombinationIterator:
    def getCombination(self):
        res = ""
        
        itr = self.itr
        s = self.s

        if itr[0]<= len(s)-len(itr):
            
            for i in itr: res+=s[i]

            if itr[-1] == len(s)-1:
                check = len(s)-1
                point = len(itr)-1
                
                while itr[point] == check:
                    check -= 1
                    point -= 1
                idx = itr[point]
                
                while point != len(itr):
                    itr[point] = idx+1
                    idx += 1
                    point += 1
            
            else:
                itr[-1] += 1
                
        return res
    
    def __init__(self, characters: str, combinationLength: int):
        self.itr = [i for i in range(combinationLength)]
        self.s = characters

    def next(self) -> str:
        return self.getCombination()

    def hasNext(self) -> bool:
        if self.itr[0]<= len(self.s)-len(self.itr):
            return True
        return False