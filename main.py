from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()

    if opening_brackets_stack:
        return opening_brackets_stack[-1].position

    return "Success"


def main():
    choice = input()
    text = input()
    mismatch = find_mismatch(text)
    choice = choice.upper()
    # Printing answer, write your code here
    if choice == "I":
        print(mismatch)
    else:
        print("Success" if mismatch == "Success" else "Mismatch")

if __name__ == "__main__":
    main()
