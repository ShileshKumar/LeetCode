class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win={}
        lose={}
        for i in matches:
            if i[0] not in win:
                win[i[0]]=0
            win[i[0]]+=1
            
            if i[1] not in lose:
                lose[i[1]]=0
            lose[i[1]]+=1
                
        noLoss=[]
        oneLoss=[]
        
        for i in win:
            if i not in lose:
                noLoss.append(i)
            
        for j in lose:
            if lose[j]==1:
                oneLoss.append(j)
                
        res=[]
        noLoss.sort()
        res.append(noLoss)        
        oneLoss.sort()
        res.append(oneLoss)
        
        return res