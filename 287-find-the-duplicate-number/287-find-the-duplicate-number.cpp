class Solution {
public:
    int findDuplicate(vector<int>& arr) {
        int n=arr.size();
        unordered_map<int,int>m;
        for(int i=0;i<n;i++) {
            m[arr[i]]++;
        }
        for(int i=0;i<n;i++) {
            if(m[arr[i]]>1) return arr[i];
        }
        return -1;
    }
};