# The country of hackerland is depicted as a graph with g_nodes cities numbered from 1 to g_nodes.
# These cities are interconnected by g_edges bidirectional roads where the ith road connects city
# g_from[i] to city g_to[i], and the fuel required to travel this road is g_weight[i] units.
#
# Vehicles in hackerland have unlimited fuel capacity, and the cost of one unit of fuel in the ith
# city is given by arr[i]. Any amount of fuel can be purchased at any city. Given two cities A and B
# determine the minimum cost to travel from A to B. If travel between them is not possible return -1.

from heapq import *

def min_cost_hackerland(g_nodes, g_from, g_to, g_weight, arr, A, B):
    neighbors = {i: set() for i in range(1, g_nodes + 1)}
    prices = [None] + arr
    weights = {}

    for i in range(len(g_from)):
        city = g_from[i]
        nextCity = g_to[i]
        nextWeight = g_weight[i]
        neighbors[city].add(nextCity)
        neighbors[nextCity].add(city)
        weights[(city, nextCity)] = nextWeight
        weights[(nextCity, city)] = nextWeight

    INF = float('inf')
    dist = [{} for _ in range(g_nodes + 1)]  # dist[city][cheapest_price] = min_cost

    dist[A][prices[A]] = 0
    priorityQueue = [(0, A, prices[A])]  # (cost, city, cheapest_price_so_far)

    while priorityQueue:
        cost, city, price = heappop(priorityQueue)

        if cost != dist[city].get(price, INF):
            continue

        if city == B:
            return cost

        for nextCity in neighbors[city]:
            nextWeight = weights[(city, nextCity)]
            nextCost = cost + price * nextWeight
            nextPrice = price if prices[nextCity] >= price else prices[nextCity]  # update running cheapest price

            if nextCost < dist[nextCity].get(nextPrice, INF):
                dist[nextCity][nextPrice] = nextCost
                heappush(priorityQueue, (nextCost, nextCity, nextPrice))

    return -1

if __name__ == "__main__":
    g_nodes = 4
    g_from  = [1, 1, 2, 3]
    g_to    = [2, 3, 3, 4]
    g_weight= [5, 2, 2, 3]   # fuel needed per road
    arr     = [7, 5, 3, 6]   # fuel price per city (1,2,3,4)

    A = 1
    B = 4
    print(min_cost_hackerland(g_nodes, g_from, g_to, g_weight, arr, A, B))