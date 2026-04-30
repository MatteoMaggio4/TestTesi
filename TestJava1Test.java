import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestJava1Test {

    @Test
    void testCompareNamesEqualStrings() {
        String a = new String("Mario");
        String b = new String("Mario");
        assertTrue(TestJava1.compareNames(a, b), "Due oggetti String distinti ma con lo stesso contenuto dovrebbero essere considerati uguali.");
    }

    @Test
    void testCompareNamesDifferentStrings() {
        String a = "Mario";
        String b = "Luigi";
        assertFalse(TestJava1.compareNames(a, b), "Due stringhe con contenuto diverso dovrebbero essere considerate diverse.");
    }

    @Test
    void testCompareNamesOneNull() {
        String a = "Mario";
        assertFalse(TestJava1.compareNames(a, null), "Una stringa e null dovrebbero essere considerate diverse.");
    }

    @Test
    void testCompareNamesBothNull() {
        assertTrue(TestJava1.compareNames(null, null), "Due stringhe null dovrebbero essere considerate uguali.");
    }

    @Test
    void testCompareNamesStringLiteralEquality() {
        String a = "Mario";
        String b = "Mario";
        assertTrue(TestJava1.compareNames(a, b), "Due stringhe letterali con lo stesso contenuto dovrebbero essere considerate uguali.");
    }

    @Test
    void testCompareNamesNewStringAndLiteral() {
        String a = new String("Mario");
        String b = "Mario";
        assertTrue(TestJava1.compareNames(a, b), "Un oggetto String creato con new e una stringa letterale con lo stesso contenuto dovrebbero essere considerati uguali.");
    }
}