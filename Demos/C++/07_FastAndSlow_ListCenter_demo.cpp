#include <iostream>

struct Node
{
    int value;
    Node* next;

    Node(int value): value(value), next(nullptr) {};
};

void PrintList(Node* head)
{
    Node* node = head;
    while (node != nullptr)
    {
        std::cout << node->value << " ";
        node = node->next;
    }
    std::cout << std::endl;
}

Node* FindListCenter(Node* head)
{
    Node* slow = head;
    Node* fast = head;

    while (fast != nullptr && fast->next != nullptr)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    return slow;
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
    head->next->next->next->next->next->next = new Node(7);

    // Find list middle value
    PrintList(head);

    Node* middle = FindListCenter(head);

    std::cout << "\nMiddle value: " << middle->value << std::endl;
    return 0;
}