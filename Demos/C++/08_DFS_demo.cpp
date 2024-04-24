#include <iostream>
#include <vector>

struct Node
{
    int value;
    Node* left;
    Node* right;

    Node(int value): value(value), left(nullptr), right(nullptr) {};
};

void DFSIterative(Node* root, std::vector<int> &visited_values)
{
    std::vector<Node*> pending = {root};

    while (pending.size() > 0)
    {
        Node* node = pending.back();
        pending.pop_back();

        visited_values.push_back(node->value);

        if (node->right != nullptr)
        {
            pending.push_back(node->right);
        }

        if (node->left != nullptr)
        {
            pending.push_back(node->left);
        }
    }
}

void DFSRecursive(Node* root, std::vector<int> &visited_values)
{
    if (root == nullptr) {
        return;
    }

    visited_values.push_back(root->value);

    DFSRecursive(root->left, visited_values);
    DFSRecursive(root->right, visited_values);
}

void PrintVector(std::vector<int> &nums)
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

    std::vector<int> dfs_iterative_output;
    DFSIterative(tree, dfs_iterative_output);
    PrintVector(dfs_iterative_output);

    std::vector<int> dfs_recursive_output;
    DFSRecursive(tree, dfs_recursive_output);
    PrintVector(dfs_iterative_output);

    return 0;
}