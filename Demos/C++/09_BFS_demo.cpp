#include <iostream>
#include <vector>

struct Node
{
    int value;
    Node* left;
    Node* right;

    Node(int value): value(value), left(nullptr), right(nullptr) {};
};

void BFSIterative(Node* root, std::vector<int> &visited_values)
{
    std::vector<Node*> pending = {root};
    
    while (pending.size() > 0)
    {
        Node* node = pending.front();
        pending.erase(pending.begin());

        visited_values.push_back(node->value);

        if (node->left != nullptr)
        {
            pending.push_back(node->left);
        }

        if (node->right != nullptr)
        {
            pending.push_back(node->right);
        }
    }
}

void BFSRecursive(Node* root, std::vector<Node*> &pending, std::vector<int> &visited_values)
{
    if (root == nullptr)
    {
        return;
    }

    visited_values.push_back(root->value);

    pending.push_back(root->left);
    pending.push_back(root->right);

    if (pending.size() > 0)
    {
        Node* node = pending.front();
        pending.erase(pending.begin());
        BFSRecursive(node, pending, visited_values);
    }
}

void PrintVector(std::vector<int> nums)
{
    for (int num : nums)
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;
}

int main()
{
    Node* tree;

    tree = new Node(1);

    tree->left = new Node(2);
    tree->right = new Node(3);

    tree->left->left = new Node(4);
    tree->left->right = new Node(5);
    tree->right->left = new Node(6);
    tree->right->right = new Node(7);

    std::vector<int> bfs_iterative_output;
    BFSIterative(tree, bfs_iterative_output);
    PrintVector(bfs_iterative_output);

    std::vector<int> bfs_recursive_output;
    std::vector<Node*> pending;
    BFSRecursive(tree, pending, bfs_recursive_output);
    PrintVector(bfs_recursive_output);

    return 0;
}