# Amazon allows customers to add reviews for the products they bought from
# their store. The review must follow Amazon's community guidelines in order
# to be published.
# 
# Suppose that Amazon has marked n strings that are prohibited in reviews.
# They assign a score to each review that denotes how well it follows the
# guidelines. The score of a review is defined as the longest contiguous
# substring of the review which does not contain any string among the list of
# n prohibited strings. A string contains a prohibited word if it has a
# contiguous substring that matches a word from the prohibited list, ignoring
# the case.
# 
# Given a review and a list of prohibited strings, calculate the review score.
# 
# Example:
# review = "GoodProductButScrapAfterWash"
# prohibitedWords = ["crap", "odpro"]
# expectedOutput = 15, as "dProductButScra" is the longest substring without 
#                      prohibited words in the review.
# 

def ComputeReviewScore(review, prohibitedWords):
    # Tranform review string to lower case
    review = review.lower()
    
    # Find the intervals where our prohibited words appear in the review
    intervals = []
    for i in range(len(review)):
        for word in prohibitedWords:
            if review[i:].startswith(word):
                intervals.append([i, i + len(word)])

    # If there are no intervals, that means that no prohibited words were found,
    # return early
    if not intervals:
        return len(review)
    
    # Sort the intervals
    intervals.sort()
    
    # Compute the max distance by comparing the intervals
    maxDistance = max(intervals[0][1], len(review) - intervals[-1][0] - 1)

    for i in range(len(intervals) - 1):
        maxDistance = max(maxDistance, intervals[i + 1][1] - intervals[i][0] - 2)

    return maxDistance

if __name__ == "__main__":
    # Example 1
    review = "GoodProductButScrapAfterWash"
    prohibitedWords = ["crap", "odpro"]
    expectedOutput = 15
    output = ComputeReviewScore(review, prohibitedWords)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    review = "FastDeliveryOkayProduct"
    prohibitedWords = ["eryoka", "yo", "eli"]
    expectedOutput = 11
    output = ComputeReviewScore(review, prohibitedWords)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 3
    review = "ExtremeValueForMoney"
    prohibitedWords = ["tuper", "douche"]
    expectedOutput = 20
    output = ComputeReviewScore(review, prohibitedWords)
    print(output, expectedOutput, output == expectedOutput)