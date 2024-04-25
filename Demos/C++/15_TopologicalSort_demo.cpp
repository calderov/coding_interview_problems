#include <unordered_map>
#include <iostream>
#include <vector>

#define graph_t std::unordered_map<int, std::vector<int>>

graph_t BuildGraph(int vertices, std::vector<std::vector<int>> edges)
{
    graph_t graph;
    for (std::vector<int> edge : edges)
    {
        int u = edge[0];
        int v = edge[1];
        
        if (graph.find(u) == graph.end())
        {
            graph[u] = {};
        }
        graph[u].push_back(v);
    }
    return graph;
}

std::unordered_map<int, int> BuildInDegreeTracker(graph_t graph)
{
    std::unordered_map<int, int> inDegree;

    for (std::pair<const int, std::vector<int>> pair : graph)
    {
        inDegree[pair.first] = 0;
    }


    for (std::pair<const int, std::vector<int>> pair : graph)
    {
        for (int v : pair.second)
        {
            inDegree[v]++;
        }
    }

    return inDegree;
}

std::vector<int> TopologicalSort(int vertices, std::vector<std::vector<int>> edges)
{
    graph_t graph = BuildGraph(vertices, edges);
    std::unordered_map<int, int> inDegree = BuildInDegreeTracker(graph);

    // Find initial sources (nodes with no incoming edges)
    std::vector<int> sources;
    for (std::pair<int, int> pair : inDegree)
    {
        if (inDegree[pair.first] == 0)
        {
            sources.push_back(pair.first);
        }
    }

    std::vector<int> sortedVertices;
    while (sources.size() > 0)
    {
        int u = sources.front();
        sources.erase(sources.begin());

        sortedVertices.push_back(u);

        // For each vertex v, children of u, decrease the inDegree value of v by one.
        // If the inDegree value of v has reached zero, add v to the sources list
        for (int v : graph[u])
        {
            inDegree[v]--;
            if (inDegree[v] == 0)
            {
                sources.push_back(v);
            }
        }
    }

    // Return an empty list if the graph is not acyclical
    if (sortedVertices.size() != vertices)
    {
        return {};
    }
    
    // Otherwise, return sorted vertices
    return sortedVertices;
}

void PrintVector(std::vector<int> nums)
{
    for (int num : nums)
    {
        std::cout << num << " ";
    }
}
int main()
{
    int vertices = 4;
    std::vector<std::vector<int>> edges = {{0, 1}, {1, 2}, {2, 3}};
    std::vector<int> expectedOutput = {0, 1, 2, 3};
    std::vector<int> output = TopologicalSort(vertices, edges);
    
    std::cout << "Topological order:" << std::endl;
    PrintVector(output);
    
    std::cout << std::endl;

    std::cout << "\nExpected order:" << std::endl;
    PrintVector(expectedOutput);
}