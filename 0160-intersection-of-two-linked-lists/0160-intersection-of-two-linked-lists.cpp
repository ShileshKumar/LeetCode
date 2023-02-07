/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *temp = headA;
        unordered_map<ListNode*, int> m;
        
        while(temp) {
            m[temp]++;
            temp = temp -> next;
        }
        
        temp = headB;
        
        while(temp) {
            if(m[temp]!=0) return temp;
            temp = temp -> next;
        }
        return NULL;
        
    }
};