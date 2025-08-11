# 346. Moving Average from Data Stream (Easy)
# Given a stream of integers and a window size, calculate the moving average
# of all integers in the sliding window.
# 
# Implement the MovingAverage class:
# - MovingAverage(int size) Initializes the object with the size of the
# window size.
# - double next(int val) Returns the moving average of the last size values
# of the stream.
#  
# Example:
#     MovingAverage movingAverage = new MovingAverage(3);
#     movingAverage.next(1); // return 1.0 = 1 / 1
#     movingAverage.next(10); // return 5.5 = (1 + 10) / 2
#     movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
#     movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
#  
# 
# Constraints:
# - 1 <= size <= 1000
# - -105 <= val <= 105
# - At most 104 calls will be made to next.

from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.window = deque()
        self.windowSum = 0
        self.size = size

    def next(self, val):
        self.window.append(val)
        self.windowSum += val

        while len(self.window) > self.size:
            self.windowSum -= self.window.popleft()

        return self.windowSum / (min(len(self.window), self.size))

if __name__ == "__main__":
    movingAverage = MovingAverage(3)
    print("%.2f %.2f" % (movingAverage.next(1), 1.0))
    print("%.2f %.2f" % (movingAverage.next(10), 5.5))
    print("%.2f %.2f" % (movingAverage.next(3), 4.66667))
    print("%.2f %.2f" % (movingAverage.next(5), 6.0))