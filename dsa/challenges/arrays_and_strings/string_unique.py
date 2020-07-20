# create a string of unique charcaters
def string_unique(the_string):
    if len(the_string)>256:
        return False
    chr_set = {}
    for chr in the_string:
        if chr in chr_set:
            return False
        chr_set[chr] = True
    return True



if __name__ == "__main__":
    the_string = "cheking"
    print(string_unique(the_string))
