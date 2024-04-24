#include <iostream>

struct Node {
    int value;
    Node* next;

    Node(int value): value(value), next(nullptr) {};
};

bool HasCycle(Node* head)
{
    Node* fast = head;
    Node* slow = head;

    while (true)
    {
        if (fast == nullptr || fast->next == nullptr || fast->next->next == nullptr)
        {
            return false;
        }

        fast = fast->next->next;
        slow = slow->next;

        if (slow == fast)
        {
            return true;
        }
    }

}

int main()
{
    // Insert elements
    Node* head;
    head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);
    head->next->next->next->next = new Node(5);
    head->next->next->next->next->next = new Node(6);

    // Insert loop (point tail to the 3rd element of the list)
    head->next->next->next->next->next->next = head->next->next;

    bool hasCycle = HasCycle(head);
    std::cout << "Is there a cycle in the list?: " << hasCycle << std::endl;

    return 0;
}