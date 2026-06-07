/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head) {
            return;
        }
        // Solution: break the list in half with slowPtr and fastPtr
        ListNode* slowPtr = head;
        ListNode* fastPtr = head->next;
        while( fastPtr && fastPtr->next) {
            slowPtr = slowPtr->next;
            fastPtr = fastPtr->next->next;
        }
        // Second list starts at slowPtr.next
        ListNode* second = slowPtr->next;
        slowPtr->next = nullptr;
        ListNode* prev = nullptr;
        // Reverse the second list
        while (second) {
            ListNode* nxt = second->next;
            second->next = prev;
            prev = second;
            second = nxt;
        }
        // Now merge them back:
        ListNode* first = head;
        second = prev;
        
        while (second ) {
            ListNode* nxt1= first->next;
            ListNode* nxt2 = second->next;
            first->next = second;
            second->next = nxt1;
            first = nxt1;
            second = nxt2;
        }
    }
};
