from stack_and_queue.stack_and_queue import Stack, Queue

"""
Write a function called validate brackets
Arguments: string
Return: boolean
representing whether or not the brackets in the string are balanced

{}	                    TRUE
{}(){}	                TRUE
()[[Extra Characters]]	TRUE
(){}[[]]	            TRUE
{}{Code}[Fellows](())	TRUE
[({}]	                FALSE
(](	                    FALSE
{(})	                FALSE
"""


def validate_brackets(text):
    opening_stack = Stack()
    op_len = 0
    closing_stack = Stack()
    closing_queue = Queue()
    clo_len = 0
    text_list = list(text)
    for i in text:
        if i == "(" or i == "{" or i == "[":
            opening_stack.push(i)
            op_len += 1
        elif i == ")" or i == "}" or i == "]":
            # closing_queue.enqueue(i)
            closing_stack.push(i)
            clo_len += 1

    # reversed_text = text_list[::-1]
    # for i in reversed_text:
    #     if i == ")" or i == "}" or i == "]":
    #         # closing_stack.push(i)
    #         closing_queue.enqueue(i)
    #         clo_len += 1

    # print(opening_stack)
    # print(closing_stack)

    if op_len == clo_len:
        for i in range(op_len):
            # print("while loop")
            if opening_stack.top.value + closing_stack.top.value == "[]" or opening_stack.top.value + closing_stack.top.value == "()" or opening_stack.top.value + closing_stack.top.value == "{}":
                # print("comparing the stacks elements")
                opening_stack.pop()
                closing_stack.pop()
            else:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    # True
    print(validate_brackets("{}"))
    print(validate_brackets("{}(){}"))
    print(validate_brackets("()[[Extra Characters]]"))
    print(validate_brackets("(){}[[]]"))
    print(validate_brackets("{}{Code}[Fellows](())"))
    #False
    print(validate_brackets("[({}]"))
    print(validate_brackets("(]("))
    print(validate_brackets("{(})"))
    print(validate_brackets("l{ama{student})}"))
    print(validate_brackets("{"))


