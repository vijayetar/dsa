package java_challenges.utilities;

public class Dog extends Animal {
    private String name;
    public Dog() {
    }
    public Dog(String name){
        this.name = name;
    }

    public String toString(){
        return "dog name: "+ name;
    }
}
