from dsa.challenges.hashtable.linked_list_hashtable import LinkedList

class Hashtable():
    '''
    This class is to implement the hashmap in python
    '''
    def __init__(self, size):
        self.size = size
        #this is creating a list of buckets to put the hashtable
        self.indices = [None]*self.size

    def hash(self, string):
        if not isinstance(string,str):
            string = str(string)
        get_ord = sum((map(lambda x: ord(x), string)))
        print("this is get_ord", get_ord)
        hashed_key = (get_ord*19)%self.size
        print(hashed_key)
        return hashed_key

    def add(self, key, value):
        '''
        adding a key and value to a node of a linked list where the pair is added as an array
        '''
        hashed_key = self.hash(key)
        if not self.indices[hashed_key]:
            self.indices[hashed_key]=LinkedList()
        self.indices[hashed_key].append([key, value])

    def get(self, key):
        '''
        takes in the key and returns the value from the hashtable
        '''
        if self.contains(key):
            hashed_key= self.hash(key)
        my_list = self.indices[hashed_key].display()
        for pair in my_list:
            if pair[0]==key:
                return pair[1]

    def contains(self,key):
        '''
         takes in the key and returns a boolean, indicating if the key exists in the table already.
        '''
        hashed_key= self.hash(key)
        if not self.indices[hashed_key]:
            raise ValueError ("key is not in the hashtable")
        my_list = self.indices[hashed_key].display()
        for pair in my_list:
            if pair[0]==key:
                return True
        return False

    def __str__(self):
        switch = False
        string = ""
        for item in self.indices:
            if item:
                switch = True
                string += ("").join(str(e) for e in item.display())
        if not switch:
            return "None"
        return string
        # return self.indices

if __name__ == "__main__":
    attempt = Hashtable(10)
    attempt.add("JB",27)
    print(attempt)
    # print(attempt.get("JB"))
    # attempt.add("BJ", 45)
    # print(attempt.contains("JB"))
    # print(attempt.get("BJ"))
    # print(attempt)
