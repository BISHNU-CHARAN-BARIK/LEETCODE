/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    struct ListNode* prev;
    struct ListNode* curr=head;
    int i,length=0,rk;
    if(head==NULL){
        return head;
    }
    if(head->next==NULL){
        return head;
    }
    while(curr!=NULL)
    {
        curr=curr->next;
        length++;
    }
    rk=k%length;
    curr=head;
    for(i=0;i<rk;i++)
    {
        prev=NULL;
        while(curr->next!=NULL)
        {
            prev=curr;
            curr=curr->next;
        }
        prev->next=NULL;
        curr->next=head;
        head=curr;
    }
    return head;
}