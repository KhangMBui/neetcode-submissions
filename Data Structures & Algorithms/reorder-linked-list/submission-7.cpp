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
        // Solution: Create a list and use two pointers
        vector<ListNode*> nodes;
        ListNode* curr = head;
        while (curr) {
            nodes.push_back(curr);
            curr = curr->next;
        }
        int l = 0, r = nodes.size() - 1;
        while (l < r) {
            nodes[l]->next = nodes[r];
            l++;
            if (l >= r) {
                break;
            }
            nodes[r]->next = nodes[l];
            r--;
        }
        nodes[r]->next = nullptr;
    }
};
