package java_challenges.utilities;

public class Other extends Animal{
    private String name;
    public Other(){}
    public Other (String name){
        this.name=name;
    }
    public String toString(){
        return "other name: "+name;
    }
}
