public class TestJava1 {
    public static boolean compareNames(String name1, String name2) {
        // BUG: In Java le stringhe si confrontano con .equals()
        // Questo codice restituirà false per due oggetti String diversi ma con lo stesso testo.
        return name1 == name2;
    }

    public static void main(String[] args) {
        String a = new String("Mario");
        String b = new String("Mario");
        System.out.println(compareNames(a, b));
    }
}