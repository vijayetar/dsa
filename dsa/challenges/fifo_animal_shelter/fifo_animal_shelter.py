
class Node:
    def __init__ (self, value, next_ = None):
        self.value = value
        if not isinstance(next_,Node) and next_ != None:
            raise TypeError("hey there is a problem with the value")
        self.next = next_

    def __str__(self):
        return f"{self.value} : {self.next}"

    def __repr__(self):
        return f"{self.value} : {self.next}"

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, new_value):
        '''Takes any value as an argument and adds a new node with that value to the back of the queue '''
        if self.isEmpty():
            self.rear = Node(new_value)
            self.front = self.rear
            return
        current = self.rear
        current.next = Node(new_value)
        self.rear = current.next
        return

    def dequeue(self):
        '''Removes the node from the front of the queue, and returns the node’s value'''
        if not self.front:
            raise Exception("this is an empty Queue")
        current = self.front
        if current.next:
            self.front = current.next
        else:
            self.front = None
            self.rear = None
        return current.value

    def peek(self):
        '''Returns the value of the node located in the front of the queue'''
        if self.isEmpty():
            raise Exception("sorry, the Queue is empty")
        return self.front.value

    def isEmpty(self):
        '''returns True if the Queue is empty '''
        if not self.front:
            return True
        return False

    def __str__(self):
        """ { a } -> { b } -> { c } -> NULL """

        final_string = ""

        current = self.front

        while current:
            final_string += f"{{{current.value}}} -> "
            current = current.next

        return f"{final_string}NULL"


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


class AnimalShelter2():
    def __init__(self):
        self.shelter_in = Queue()
        self.shelter_out= Queue()

    def enqueue(self, animal):
        '''Takes type of animal as an argument and adds a new node with that name to the back of the animal queue'''
        self.shelter_in.enqueue(animal)
        return

    def dequeue(self, pref):
        '''Takes in argument pref of either cat, dog or other animal and removes the node from the front of the animal queue, and returns the node’s value.'''
        if self.shelter_in.isEmpty():
            raise Exception("Canot Dequeue. Shelter is Empty")
        return_node = None
        while not self.shelter_in.isEmpty():
            front_line = self.shelter_in.dequeue()
            if pref == front_line:
                if return_node == None:
                    return_node = front_line
                else:
                    self.shelter_out.enqueue(front_line)
            else:
                self.shelter_out.enqueue(front_line)
        self.shelter_in, self.shelter_out = self.shelter_out, self.shelter_in
        if not return_node:
            return f"We do not have your preference {pref}"
        return f"We have your preferred {pref} : {return_node}"


    def isEmpty(self):
        '''returns True if the Animal Shelter is empty '''
        if not self.shelter_in.front:
            return True
        return False

    def peek(self):
        '''Takes one argument pref of animal type, and returns the value of the node located in the front of the pref animal queue'''
        if self.shelter_in.isEmpty():
            return "Nothing to Peek. Shelter is Empty"
        return self.shelter_in.front.value

    def __str__(self):
        final_string = ""
        current = self.shelter_in.front
        while current:
            final_string += f"{{{current.value}}} -> "
            current = current.next

        return f"{final_string}NULL"

if __name__ == "__main__":
        ssh = AnimalShelter2()
        ssh.enqueue("dog")
        ssh.enqueue("cat")
        ssh.enqueue("otter")
        ssh.enqueue("snake")
        ssh.enqueue("cat")
        print(str(ssh))
        print(ssh.dequeue("cat"))
        print(str(ssh))
        print(ssh.shelter_out.isEmpty())
        print(ssh.shelter_in.isEmpty())
        print(ssh.dequeue("otter"))
        print(str(ssh))
        print(ssh.shelter_out.isEmpty())
        print(ssh.shelter_in.isEmpty())
        print(ssh.dequeue("rabbit"))
        print(str(ssh))
        print(ssh.shelter_out.isEmpty())
        print(ssh.shelter_in.isEmpty())

