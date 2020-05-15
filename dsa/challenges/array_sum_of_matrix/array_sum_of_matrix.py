def sum_of_matrix_array(matrix):
    """ sum of values in given array of array of numbers """
    if len(matrix)== 0:
        return "incorrect input"
    new_list = list()
    for arr in matrix:
        sum = 0
        for num in arr:
            if num == "":
                sum += 0
            else:
                sum += num
        new_list.append(sum)
    return new_list



if __name__ == "__main__":
    pass
