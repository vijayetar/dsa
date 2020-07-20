from dsa.data_structures.stack_and_queues.stack_and_queues import Node, Stack

def multi_bracket_validation(input_string):
    br_dict = {'}':'{', ')':"(", ']':"["}
    if input_string == "":
        return False
    _stack = Stack()
    _stack_length = 0
    for chr in input_string:
        if chr in br_dict:
            if br_dict[chr]==_stack.peek():
                _stack.pop()
            else:
                return False
        elif chr in br_dict.values():
            _stack.push(chr)
            _stack_length += 1
    if _stack_length == 0:
        return "no brackets in string"
    elif _stack.isEmpty():
        return True
    return False


def matching_brackets(string):
    bracket = Stack()
    bracket_dict = {"(":")","{":"}", "[":"]" }
    for char in string:
        if char in bracket_dict:
            bracket.push(char)
        elif char in [")", "}", "]"]:
            if bracket.isEmpty():
                return False
            if bracket_dict[bracket.peek()]==char:
                bracket.pop()
            else:
                return False
    if not bracket.isEmpty():
        return False
    return True


if __name__ == "__main__":
    # input_string = "jjkjklj"
    input_string = "abcds{([])}"
    print(multi_bracket_validation(input_string))
