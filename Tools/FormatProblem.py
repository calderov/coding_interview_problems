#! /usr/bin/env python
import clipboard

def format_text_to_python_comment_of_80_cols(text):
    lines = text.split('\n')
    formattedLines = []

    for line in lines:
        if len(line) < 78:
            formattedLines.append("# " + line + "\n")
            continue

        words = line.split(" ")
        newLine = "#"
        while words:
            word = words.pop(0) 
            if len(word) > 78 or len(newLine) + len(word) + 1 < 78:
                newLine = newLine + " " + word
            else:
                formattedLines.append(newLine + "\n")
                words.insert(0, word)
                newLine = "#"
        
        formattedLines.append(newLine + "\n")
    
    return "".join(formattedLines)

if __name__ == "__main__":
    text = clipboard.paste()
    text = text.replace("\r", "")
    formatted_text = format_text_to_python_comment_of_80_cols(text)
    print(formatted_text)
    clipboard.copy(formatted_text)
