package java_challenges.utilities;

import java.util.HashSet;
import java.util.LinkedList;

public class AnimalShelterByNich {
    // this has O1 for dequeue and On for space
    LinkedList<Animal> animals = new LinkedList<>();
    LinkedList<Cat> cats = new LinkedList<>();
    LinkedList<Dog> dogs = new LinkedList<>();
    HashSet<Animal> adoptedAnimals = new HashSet<>();
    public void enQueue(Cat cat){
        animals.add(cat);
        cats.add(cat);
    }
    public void enQueue(Dog dog){
        animals.add(dog);
        dogs.add(dog);
    }
    public Animal deQueue(){
        Animal animal = animals.removeFirst();
        while (adoptedAnimals.contains(animal)){
            animal = animals.removeFirst();
        }
        return animal;
    }
    public Animal dequeue(Class<?> cl) throws ClassNotFoundException {
        if (cl == Cat.class){
            Cat adoptee = cats.removeFirst();
            adoptedAnimals.add(adoptee);
            return adoptee;

        } else if (cl == Dog.class){
            Dog adoptee = dogs.removeFirst();
            adoptedAnimals.add(adoptee);
            return adoptee;

        } else{
            throw new ClassNotFoundException("We only have cats and dogs!");

        }
    }


}
