class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int t=m+n-1;
        while(m-1>=0 && n-1>=0) {
            if(nums1[m-1]>nums2[n-1]) {
                nums1[t]=nums1[m-1];
                m--;
                t--;
            }
            else {
               nums1[t]=nums2[n-1];
                n--;
                t--;
            }
        }
        while(n>0) {
            nums1[t]=nums2[n-1];
            n--;
            t--;
        }
        //return nums1
    }
};