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


def validate_brackets(shape):
    shapes = ["{}", "[]", "()"]
    stack = Stack()
    for bracket in shape:
        if bracket == "{" or bracket == "(" or bracket == "[":
            stack.push(bracket)
        elif bracket == "}" or bracket == ")" or bracket == "]":
            if stack.top is None:
                return False
            elif (stack.top.value + bracket) in shapes:
                stack.pop()
            else:
                return False
    return True if stack.isEmpty() else False


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


