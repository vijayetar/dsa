def is_repeated_letter(string):
	unique_dict = {}
	for chr in string:
	  if chr.lower() in unique_dict:
		  return False
	  unique_dict[chr.lower()]=0
	return True

if __name__ == "__main__":
    print(is_repeated_letter("string"))
