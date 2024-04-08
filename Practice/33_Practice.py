# 981. Time Based Key-Value Store (Medium)
# Design a time-based key-value data structure that can store multiple values
# for the same key at different time stamps and retrieve the key's value at a
# certain timestamp.
# 
# Implement the TimeMap class:
# - TimeMap()
#  
# - void set(String key, String value, int timestamp)
#  
# - String get(String key, int timestamp)
# 
# Example:
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along
# with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value
# corresponding to foo at timestamp 3 and timestamp 2, then the only value is
# at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2"
# along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
#  
# 
# Constraints:
# - 1 <= key.length, value.length <= 100
# - key and value consist of lowercase English letters and digits.
# - 1 <= timestamp <= 107
# - All the timestamps timestamp of set are strictly increasing.
# - At most 2 * 105 calls will be made to set and get.


class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []

        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.data or key not in self.data:
            return ""
        
        if timestamp < self.data[key][0][0]:
            return ""
        
        low = 0
        high = len(self.data[key]) - 1

        prevIndex = -1

        while low <= high:
            mid = (low + high) // 2

            midTimestamp, midValue = self.data[key][mid]

            if midTimestamp == timestamp:
                return midValue
            
            if midTimestamp < timestamp:
                prevIndex = max(prevIndex, mid)
                low = mid + 1

            else: # midTimestamp > timestamp
                high = high - 1

        if prevIndex != -1:
            return self.data[key][prevIndex][1]

        return ""

if __name__ == "__main__":
    timeMap = TimeMap()

    timeMap.set(1, "a", 1)
    timeMap.set(1, "b", 2)
    timeMap.set(1, "c", 3)
    timeMap.set(1, "d", 4)
    timeMap.set(1, "e", 5)

    print(timeMap.get(1, 1), "a")
    print(timeMap.get(1, 2), "b")
    print(timeMap.get(1, 3), "c")
    print(timeMap.get(1, 4), "d")
    print(timeMap.get(1, 5), "e")
    print(timeMap.get(1, 6), "e")

    print("Done")