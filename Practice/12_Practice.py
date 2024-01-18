# Given a string s made only of English characters return the lenght of the last word
# Example
# 
#   input = "  fly me to the moon "
#   output = 4
#   
#   Explaination: "moon" is the last word in the string and it has 4 letters

def GetLastWordLenght(inputString: str):  
    i = len(inputString) - 1
    count = 0

    while i >= 0:
        if inputString[i] == ' ' and count:
            return count
        
        if inputString[i] != ' ':
            count += 1
        
        i -= 1
    
    return count

if __name__ == "__main__":
    inputString = "  fly me to the moon "
    expectedOutput = 4
    output = GetLastWordLenght(inputString)
    print(output, expectedOutput, output == expectedOutput)
    print("foo")