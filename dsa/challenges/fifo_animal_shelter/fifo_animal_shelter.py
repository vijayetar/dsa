from dsa.data_structures.stack_and_queues.stack_and_queues import Node, Queue

class AnimalShelter():
    def __init__(self):
        self._dog_shelter = Queue()
        self._cat_shelter = Queue()
        self._others_shelter = Queue()

    def enqueue(self, animal, name):
        '''Takes type of animal and name as an argument and adds a new node with that name to the back of the animal queue'''
        if animal == "dog":
            self._dog_shelter.enqueue(name)
            return
        elif animal == "cat":
            self._cat_shelter.enqueue(name)
            return
        string = f"{animal}-{name}"
        self._others_shelter.enqueue(string)
        return

    def dequeue(self, pref):
        '''Takes in argument pref of either cat, dog or other and removes the  from the front of the animal queue, and returns the node’s value.'''
        if pref == "dog":
            return self._dog_shelter.dequeue()
        elif pref == "cat":
            return self._cat_shelter.dequeue()
        return self._others_shelter.dequeue()

    def isEmpty(self):
        '''returns True if the Animal Shelter is empty '''
        return self._cat_shelter.isEmpty() and self._dog_shelter.isEmpty() and self._others_shelter.isEmpty()

    def peek(self, pref):
        '''Takes one argument pref of animal type, and returns the value of the node located in the front of the pref animal queue'''
        if pref == "dog":
            return self._dog_shelter.peek()
        elif pref == "cat":
            return self._cat_shelter.peek()
        return self._others_shelter.peek()

    def __str__(self):
        ''' '''
        final_string = ""
        if not self._dog_shelter.isEmpty():
            final_string+= f"DOGS: {str(self._dog_shelter)} "
        if not self._cat_shelter.isEmpty():
            final_string+= f"CATS: {str(self._cat_shelter)} "
        if not self._others_shelter.isEmpty():
            final_string+= f"OTHERS: {str(self._others_shelter)} "
        return final_string


