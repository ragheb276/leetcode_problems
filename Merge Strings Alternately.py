def solution(word1,word2):
    i = 0
    j = 0
    m = len(word1)
    n = len(word2)
    result = []
    
    while i < m or j < n:
        if i < m :
            result = result + word1[i]
            i+=1
            
        if j < n :
            result = result + word2[j]
            j+=1
            
    return result

#-----------------------------------------------

def solution2(word1,word2):
    i = 0
    m = len(word1)
    n = len(word2)
    result = []
    
    while i < m or i < n:
        if i < m :
            result = result + word1[i]
            
            
        if i < n :
            result = result + word2[i]
    i+=1
            
    return result

#-------------------------------------------------
def solution3(word1,word2):
    i = 0
    n = max(len(word1),len(word2))
    result = []
    
    for i in range(n):
        if i < len(word1) :
            result = result + word1[i]
            
            
        if i < len(word2) :
            result = result + word2[i]
    
            
    return result
