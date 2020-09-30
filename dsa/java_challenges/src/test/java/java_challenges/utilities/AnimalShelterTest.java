package java_challenges.utilities;
// reference : https://stackoverflow.com/questions/6271417/java-get-the-current-class-name for .getClass().getSimpleName()
import org.junit.Test;

import static org.junit.Assert.*;

public class AnimalShelterTest {
    @Test
    public void testAnimalShelterInstantiation(){
        AnimalShelter animalShelter = new AnimalShelter();
        assertTrue("this is empty", animalShelter.isEmpty());
    }
    @Test
    public void testAnimalShelterInstantiationNoFront(){
        AnimalShelter animalShelter = new AnimalShelter();
        assertEquals("NULL", animalShelter.toString());
    }
    @Test public void testEnqueueNewAnimalToFront(){
        AnimalShelter animalShelter = new AnimalShelter();
        animalShelter.enqueue(new Cat("Garfield"));
        assertEquals("{cat name: Garfield}", animalShelter.getFront().toString());
    }
    @Test public void testEnqueueNewAnimalToFrontReturnClass(){
        AnimalShelter animalShelter = new AnimalShelter();
        animalShelter.enqueue(new Cat("Garfield"));
        AnimalShelter.Node<Animal> inFront = animalShelter.getFront();
        assertEquals("Cat", inFront.value.getClass().getSimpleName());
    }
    @Test public void testEnqueueMultipleAnimals(){
        AnimalShelter animalShelter = new AnimalShelter();
        animalShelter.enqueue(new Dog("Pluto"));
        animalShelter.enqueue(new Cat("Garfield"));
        animalShelter.enqueue(new Cat("Tom"));
        animalShelter.enqueue(new Dog("Lucky"));
        animalShelter.enqueue(new Cat("Snowbell"));
        AnimalShelter.Node<Animal> inFront = animalShelter.getFront();
        assertEquals("Dog", inFront.value.getClass().getSimpleName());
        assertEquals("dog name: Pluto <= cat name: Garfield <= cat name: Tom <= dog name: Lucky <= cat name: Snowbell <= NULL", animalShelter.toString());
    }
//    @Test public void testDequeueAtFront() {
//        AnimalShelter animalShelter = new AnimalShelter();
//        animalShelter.enqueue(new Dog("Pluto"));
//        animalShelter.enqueue(new Cat("Garfield"));
//        animalShelter.enqueue(new Cat("Tom"));
//        Dog dog = new Dog();
//        assertEquals("dog name: Pluto", animalShelter.dequeue(dog));
//    }
//    @Test public void testDequeueLast() {
//        AnimalShelter animalShelter = new AnimalShelter();
//        animalShelter.enqueue(new Dog("Pluto"));
//        animalShelter.enqueue(new Dog("Lucky"));
//        animalShelter.enqueue(new Cat("Tom"));
//        Cat cat = new Cat();
//        assertEquals("cat name: Tom", animalShelter.dequeue(cat));
//    }
    @Test public void testDequeueStringAtFront(){
        AnimalShelter animalShelter = new AnimalShelter();
        animalShelter.enqueue(new Dog("Pluto"));
        animalShelter.enqueue(new Dog("Lucky"));
        animalShelter.enqueue(new Cat("Tom"));
        assertEquals("dog name: Pluto", animalShelter.dequeue("dog"));
    }
    @Test public void testDequeueStringAtFrontCheckNewFront(){
        AnimalShelter animalShelter = new AnimalShelter();
        animalShelter.enqueue(new Dog("Pluto"));
        animalShelter.enqueue(new Dog("Lucky"));
        animalShelter.enqueue(new Cat("Tom"));
        animalShelter.dequeue("dog");
        animalShelter.dequeue("dog");
        assertEquals("{cat name: Tom}",animalShelter.getFront().toString());
    }
    @Test public void testDequeueStringAtLast(){
        AnimalShelter animalShelter = new AnimalShelter();
        animalShelter.enqueue(new Dog("Pluto"));
        animalShelter.enqueue(new Dog("Lucky"));
        animalShelter.enqueue(new Cat("Tom"));
        assertEquals("cat name: Tom", animalShelter.dequeue("cat"));
    }
    @Test public void testDequeueStringInMiddle(){
        AnimalShelter animalShelter = new AnimalShelter();
        animalShelter.enqueue(new Dog("Pluto"));
        animalShelter.enqueue(new Dog("Lucky"));
        animalShelter.enqueue(new Cat("Tom"));
        animalShelter.enqueue(new Dog("Fido"));
        animalShelter.enqueue(new Cat("Snowbell"));
        animalShelter.dequeue("cat");
        animalShelter.dequeue("dog");
        assertEquals("{dog name: Lucky}",animalShelter.getFront().toString());
        assertEquals("dog name: Lucky <= dog name: Fido <= cat name: Snowbell <= NULL", animalShelter.toString());
    }
    @Test public void testDequeueNotDogNotCat(){
        AnimalShelter animalShelter = new AnimalShelter();
        animalShelter.enqueue(new Dog("Pluto"));
        animalShelter.enqueue(new Dog("Lucky"));
        animalShelter.enqueue(new Cat("Tom"));
        animalShelter.enqueue(new Dog("Fido"));
        animalShelter.enqueue(new Cat("Snowbell"));
        assertNull("no match found", animalShelter.dequeue("lizard"));
    }
    @Test public void testDequeueEmptyShelter() {
        AnimalShelter animalShelter = new AnimalShelter();
        assertNull("empty shelter", animalShelter.dequeue("dog"));
    }
}
