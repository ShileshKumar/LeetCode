class Solution {
public:
    int longestConsecutive(vector<int>& arr) {
        int N=arr.size();
        unordered_map<int, int>mp;
        for(int i=0;i<N;i++)
        {
            mp[arr[i]]++;
        }
        int mx=0;
        for(int i=0;i<N;i++)
        {
            if(mp.find(arr[i]-1)!=mp.end())
            {
                continue;
            }
            else
            {
                int count=1;
                int element=arr[i]+1;
                while(mp.find(element)!=mp.end())
                {
                    count++;
                    element=element+1;
                }
                mx=max(mx,count);
            }
        }
        return mx;
    }
};