package java_challenges.utilities;
// reference : https://stackoverflow.com/questions/6271417/java-get-the-current-class-name for .getClass().getSimpleName()
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

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
        assertEquals("{cat name: Garfield}", animalShelter.front);
    }
}
