import os

if __name__ == "__main__":
    path = "C:\\git\\grokking_the_coding_interview\\Demos\\"

    chapters = {
        "01: Quicksort": "01_QuickSort_demo.py",
        "02: Cyclic sort": "02_CyclicSort_Demo.py",
        "03: Binary search": "03_BinarySearch_demo.py",
        "04: Reverse list": "04_ReverseLinkedList_Demo.py",
        "05: Top K emelents": "05_TopKElements_demo.py",
        "06: Fast and slow (cycle in linked list)": "06_FastAndSlow_CycleInList_demo.py",
        "07: Fast and slow (middle of linked list)": "07_FastAndSlow_ListCenter_demo.py",
        "08: DFS": "08_DFS_demo.py",
        "09: BFS": "09_BFS_demo.py",
        "10: All subsets": "10_AllSubsets_demo.py",
        "11: All permutations": "11_AllPermutations_demo.py",
        "12: Merge intervals": "12_MergeIntervals_demo.py",
        "13: Dynamic programming": "13_DynamicProgramming_demo.py",
        "14: Backtracking": "14_Backtracking_demo.py",
        "15: Topological sort": "15_TopologicalSort_demo.py",
    }

    for chapter in chapters:
        print("# Chapter", chapter)
        print("```python")
        with open(path + chapters[chapter]) as f:
            for line in f.readlines():
                print(line[:-1])
        print("```")