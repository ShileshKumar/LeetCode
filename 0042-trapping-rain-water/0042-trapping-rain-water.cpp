class Solution {
public:
    int trap(vector<int>& height) {
        int n=height.size();
        
        if(n==0) {
            return 0;
        }
        
        int maxLeft[n];
        int maxRight[n];
        
        maxLeft[0]=0;
        for(int i=1;i<n;i++) {
            maxLeft[i]=max(maxLeft[i-1],height[i-1]);
        }
        
        maxRight[n-1]=0;
        for(int i=n-2;i>=0;i--) {
            maxRight[i]=max(maxRight[i+1],height[i+1]);
        }
            
        int result=0;
        for(int i=0;i<n;i++) {
            int water_above = min(maxLeft[i],maxRight[i]) - height[i];
            if(water_above>0) {
                result+=water_above;
            }
        }
        return result;
    }
};