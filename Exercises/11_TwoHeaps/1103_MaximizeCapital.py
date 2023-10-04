# Maximize Capital (hard)
# Problem Statement
# 
# Given a set of investment projects with their respective profits, we need
# to find the most profitable projects. We are given an initial capital and
# are allowed to invest only in a fixed number of projects. Our goal is to
# choose projects that give us the maximum profit. Write a function that
# returns the maximum total capital after selecting the most profitable
# projects.
# 
# We can start an investment project only when we have the required capital.
# After selecting a project, we can assume that its profit has become our
# capital, and that we have also received our capital back.
# 
# Example 1:
# 
# Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial
# Capital=1, Number of Projects=2
# 
# Output: 6
# 
# Explanation:
# 1. With initial capital of ‘1’, we will start the second project which will
# give us profit of ‘2’. Once we selected our first project, our total
# capital will become 3 (profit + initial capital).
# 2. With ‘3’ capital, we will select the third project, which will give us
# ‘3’ profit.
# 
# After the completion of the two projects, our total capital will be 6
# (1+2+3).
# 
# Example 2:
# 
# Input: Project Capitals=[0,1,2,3], Project Profits=[1,2,3,5], Initial
# Capital=0, Number of Projects=3
# 
# Output: 8
# 
# Explanation:
# 
# 1. With ‘0’ capital, we can only select the first project, bringing out
# capital to 1.
# 2. Next, we will select the second project, which will bring our capital to
# 3.
# 3. Next, we will select the fourth project, giving us a profit of 5.
# 
# After selecting the three projects, our total capital will be 8 (1+2+5).
# 

from heapq import *

class Solution:
    # Solution:
    # 1. Initialize two empty heaps, a min-heap to store costs and a max-heap to store profits.
    #    minCosts = []
    #    maxProfits = []
    #
    # 2. Add all costs to the minCosts min-heap.
    #  
    # 3. For at most maxProjects do the following:
    #  
    #    3.1 Find all projects that can be afforded by the current capital
    #        and store them in the maxProfits max-heap (so the most profitable 
    #        project is placed on top).
    #  
    #    3.2 If there are no more affordable projects, break early. In other words,
    #        break early if maxProfits is empty.
    #  
    #    3.3 Otherwise, pop the top of maxProfits to retrieve the most profitable project
    #        that we can affort so far, and increase the capital by adding the profit of
    #        this project.
    #
    #    3.4 Repeat step 3 if we have not yet selected at most maxProjects.
    #  
    # 4. Return the final amount of capital after profits.
    #  
    # Solution complexity:
    # Time complexity: O(NlogN + KlogN) where N is the total number of projects
    #                  and K is the number of projects that we are allowed to select.
    # Space complexity: O(N) 

    def MaximizeCapital(self, costs, profits, capital, maxProjects):
        # Initialize two empty heaps, a min-heap to store costs and a max-heap to store profits
        minCosts = []
        maxProfits = []

        # Add all costs to the minCosts min-heap
        minCosts = [(costs[i], i) for i in range(len(costs))]
        heapify(minCosts)

        # For at most maxProjects
        for _ in range(maxProjects):
            # Find all projects that can be afforded by the current capital
            # and store them in the maxProfits max-heap (so the most profitable 
            # project is placed on top)
            while minCosts and minCosts[0][0] <= capital:
                projectCost, projectId = heappop(minCosts)
                heappush(maxProfits, (-profits[projectId], projectId))

            # If there are no more affordable projects, break early
            if not maxProfits:
                break

            # Increase the capital by adding the profit of the most profitable project
            projectProfit, projectId = heappop(maxProfits)
            capital += -projectProfit

        # Return the final amount of capital after profits
        return capital

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    costs = [0, 1, 2]
    profits = [1, 2, 3]
    capital = 1
    maxProjects = 2
    expectedOutput = 6
  
    output = solution.MaximizeCapital(costs, profits, capital, maxProjects)

    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    costs = [0, 1, 2, 3]
    profits = [1, 2, 3, 5]
    capital = 0
    maxProjects = 3
    expectedOutput = 8

    output = solution.MaximizeCapital(costs, profits, capital, maxProjects)

    print(output, expectedOutput, output == expectedOutput)
