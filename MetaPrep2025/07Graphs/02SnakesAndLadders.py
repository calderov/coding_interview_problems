# Snakes and Ladders: The Quickest Way Up
# https://www.hackerrank.com/challenges/the-quickest-way-up/problem

def quickestWayUp(ladders, snakes):
    goto = {}

    for source, dest in ladders:
        goto[source] = dest
    
    for source, dest in snakes:
        goto[source] = dest
        
    pending = [1]
    visited = set()
    level = 0
    
    while pending:
        n = len(pending)
        for _ in range(n):
            node = pending.pop(0)

            if node == 100:
                return level
        
            if node in visited:
                continue
    
            visited.add(node)
            
            for i in range(1, 7):
                nextNode = node + i
                
                if nextNode in goto:
                    nextNode = goto[nextNode]

                if nextNode in visited or nextNode > 100:
                    continue

                pending.append(nextNode)
                    
        level += 1
    
    # Goal unreachable
    return -1



if __name__ == "__main__":
    # Example 1
    ladders = [[32,62], [42,68], [12,98]]
    snakes = [[95,13],[97,25],[93,37],[79,27],[75,19],[49,47],[67,17]]
    expected = 3
    output = quickestWayUp(ladders, snakes)

    print(expected)
    print(output)
    print(output == expected)

    print()

    # Example 2
    ladders = [[8,52],[6,80],[26,42],[2,72]]
    snakes = [[51,19], [39,11], [37,29], [81,3], [59,5], [79,23], [53,7], [43,33], [77,21]]
    expected = 5
    output = quickestWayUp(ladders, snakes)

    print(expected)
    print(output)
    print(output == expected)

    print()