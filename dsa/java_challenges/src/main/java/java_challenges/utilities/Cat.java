package java_challenges.utilities;

public class Cat extends Animal{
    private String name;
    public Cat() {
    }
    public Cat(String name){
        this.name = name;
    }
    public String toString(){
        return "cat name: "+ name;
    }
}
