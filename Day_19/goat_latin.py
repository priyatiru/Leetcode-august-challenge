class Solution:
    def toGoatLatin(self, S: str) -> str:
        word=S.split(" ")
        index_count=1
        output=[]
        vowel= {'a','e','i','o','u'}
        for i in word:
            if i[0].lower() in vowel:
                ans=i+"ma"+("a"*index_count)
            else:
                ans=i[1:]+i[0]+"ma"+("a"*index_count)
            index_count+=1
            output.append(ans)
        return " ".join(c for c in output)