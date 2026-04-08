# Given two boxes represented by tuples of the form (top, left, botton, right) complete the IOU function below
# https://medium.com/analytics-vidhya/iou-intersection-over-union-705a39e7acef

def IntervalIntersectionLength(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    start = max(start1, start2)
    end = min(end1, end2)
    return max(0, end - start)

def IntersectionArea(box1, box2):
    top1, left1, bottom1, right1 = box1
    top2, left2, bottom2, right2 = box2

    base = IntervalIntersectionLength((left1, right1), (left2, right2))
    height = IntervalIntersectionLength((top1, bottom1), (top2, bottom2))

    return base * height

def Area(box):
    top, left, right, bottom = box
    area = abs(top - bottom) * abs(right - left)
    return area

def UnionArea(box1, box2):
    area1 = Area(box1)
    area2 = Area(box2)
    union = area1 + area2 - IntersectionArea(box1, box2)
    return union

def IOU(box1, box2):
    intersection = IntersectionArea(box1, box2)
    union = UnionArea(box1, box2)
    if union == 0:
        return 0
    return intersection / union

if __name__=="__main__":
    # Example 1
    box1 = (0, 0, 2, 2)
    box2 = (0, 0, 2, 2)
    expected = 1.0
    output = IOU(box1, box2)
    print(expected)
    print(output)
    print(output == expected)
    print()

    # Example 2
    box1 = (0, 0, 2, 2)
    box2 = (1, 1, 3, 3)
    expected = 1/7
    output = IOU(box1, box2)
    print(expected)
    print(output)
    print(output == expected)
    print()
    
    # Example 3
    box1 = (0, 0, 1, 1)
    box2 = (2, 2, 3, 3)
    expected = 0.0
    output = IOU(box1, box2)
    print(expected)
    print(output)
    print(output == expected)
    print()

    # Example 4
    box1 = (0, 0, 4, 4)
    box2 = (1, 1, 3, 3)
    expected = 0.25
    output = IOU(box1, box2)
    print(expected)
    print(output)
    print(output == expected)
    print()

    # Example 5
    box1 = (0, 0, 1, 1)
    box2 = (1, 0, 2, 1)
    expected = 0.0
    output = IOU(box1, box2)
    print(expected)
    print(output)
    print(output == expected)
    print()