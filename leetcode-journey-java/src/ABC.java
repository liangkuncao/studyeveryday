public class ABC {
    public static ABC abc;
    private ABC() {

    }

    public static ABC getInstance() {
        if (abc == null) {
            abc = new ABC();
        }
        return abc;
    }
}
