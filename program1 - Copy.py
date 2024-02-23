class Solution(object):
    def isValid(self, s:str)->bool:

    
    if len(s)%2!=0:
        return false
        dict={'(':')','[':']','{':'}'}
        stack=[]
        for i in self:
            if i in dict.keys():
                stack.append(i)
                else
                is stack==[]:
                return falsea=stack.pop()
                if i!=dict[a]:
                    return false
                    return stack==[]
                    
    



  

