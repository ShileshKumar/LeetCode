class Solution {
public:
    int climbStairs(int n) {
        int a=1;
        int b=2;
        int c=n;
        int i=3;
        while(i<=n) {
            c=a+b;
            a=b;
            b=c;
            i++;
        }
        return c;
    }
};