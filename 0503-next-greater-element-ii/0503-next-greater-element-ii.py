class Solution:
    def nextGreaterElements(self, a: List[int]) -> List[int]:
        st=[]
        ans=[]
        n=len(a)
        for i in range(n-1,-1,-1):
            st.append(a[i])
            
        for i in range(n-1,-1,-1):
            if len(st)==0:
                ans.append(-1)
            
            elif len(st)!=0 and st[-1]>a[i]:
                ans.append(st[-1])
            
            elif len(st)!=0 and st[-1]<=a[i]:
                while len(st)!=0 and st[-1]<=a[i]:
                    st.pop()
                if len(st)==0:
                    ans.append(-1)
                else:
                    ans.append(st[-1])
            st.append(a[i])
        return ans[::-1]