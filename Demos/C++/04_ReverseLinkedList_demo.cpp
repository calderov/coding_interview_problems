#include <iostream>

struct Node
{
    int value;
    Node* next;
    Node(int value) : value(value), next(nullptr) {}
};

void ReverseList(Node*& head)
{
    Node* node = head;
    Node* prevNode = nullptr;
    Node* nextNode = nullptr;

    while (node != nullptr)
    {
        nextNode = node->next;
        node->next = prevNode;
        prevNode = node;
        node = nextNode;
    }

    head = prevNode;
}

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

int main()
{
    // Build linked list with values ranging from 0 to 9
    Node* head = nullptr;
    Node* tail = nullptr;

    for (int i = 0; i < 10; i++)
    {
        Node* node = new Node(i);

        if (head == nullptr)
        {
            head = node;
            tail = node;
            continue;
        }

        tail->next = node;
        tail = node;
    }

    PrintList(head);
    ReverseList(head);
    PrintList(head);

    return 0;
}