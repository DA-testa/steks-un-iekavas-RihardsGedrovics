from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def matchc(bracket, c):
    if bracket.char == '[' and c == ']':
        return True
    if bracket.char == '{' and c == '}':
        return True
    if bracket.char == '(' and c == ')':
        return True
    return False

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
        if next in ")]}":
            if not opening_brackets_stack or not matchc(opening_brackets_stack[-1], next):
                return i + 1
            opening_brackets_stack.pop()
    return "Success" if not opening_brackets_stack else opening_brackets_stack[-1].position

def main():
    text = input()
    result = find_mismatch(text)
    if isinstance(result, int):
        print(result)
    else:
        print(result)

if __name__ == "__main__":
    main()
