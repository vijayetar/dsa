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


if __name__ == "__main__":
    # input_string = "jjkjklj"
    input_string = "abcds{([])}"
    print(multi_bracket_validation(input_string))
