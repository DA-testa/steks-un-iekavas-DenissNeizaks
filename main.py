# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    count = 0
    opening_brackets_stack = []
    opened_bracket_index = []
    for i, next in enumerate(text):
        count+=1
        if next in "([{":
            opened_bracket_index.append(count)
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if opening_brackets_stack == []:
                print (i+1)
                return False
            
            lastElement = opening_brackets_stack [len(opening_brackets_stack) - 1]
            
            if are_matching(lastElement,next)==False:
                print (i+1)
                return False
            opening_brackets_stack.pop()
            opened_bracket_index.pop(0)
            pass


    if opening_brackets_stack == []:
        return True
    else:
        print (opened_bracket_index[0])
        return False


def main():
    text = input()
    mismatch = find_mismatch(text)
    if (mismatch):
        print ("Success")
    # Printing answer, write your code 


if __name__ == "__main__":
    main()

