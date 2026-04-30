public class PalindromeChecker {
    
    public static boolean isPalindrome(String text) {
        if (text == null || text.isEmpty()) {
            return true;
        }
        
        String reversed = "";
        
        // BUG: In Java (e in quasi tutti i linguaggi) gli indici partono da 0.
        // L'ultimo carattere si trova all'indice text.length() - 1.
        // Partire da text.length() genererà una StringIndexOutOfBoundsException al primo giro.
        for (int i = text.length(); i >= 0; i--) {
            reversed += text.charAt(i);
        }
        
        return text.equals(reversed);
    }

    // Un main fittizio giusto per far compilare la classe senza problemi
    public static void main(String[] args) {
        System.out.println("Verifica: " + isPalindrome("anna"));
    }
}