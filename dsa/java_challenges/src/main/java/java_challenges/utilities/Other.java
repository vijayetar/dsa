package java_challenges.utilities;

public class Other {
    private String type;

    public Other(String type) {
        this.type = type;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    @Override
    public String toString() {
        return "Other{" +
            "type='" + type + '\'' +
            '}';
    }
}
