class Solution {
public:
    vector<int> relativeSortArray(vector<int>& a, vector<int>& b) {
        int n=a.size();
        int m=b.size();
        
        vector<int>res;
        map<int,int>mp;
        for(int i=0;i<n;i++) 
            mp[a[i]]++;
        
        for(int i=0;i<m;i++) {
            if(mp.find(b[i])!=mp.end()) //found
            {
                int freq=mp[b[i]]--;
                while(freq--)
                    res.push_back(b[i]);
                mp.erase(b[i]);
            }
        }
        for(auto i:mp) 
        {
            while(i.second--) 
                res.push_back(i.first);
        }
        return res;
    }
};