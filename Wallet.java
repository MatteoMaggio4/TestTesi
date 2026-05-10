public class Wallet {
    private double balance;
    private double dailyLimit;
    private double spentToday;

    public Wallet(double balance, double dailyLimit) {
        this.balance = balance;
        this.dailyLimit = dailyLimit;
        this.spentToday = 0.0;
    }

    public double pay(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("L'importo deve essere maggiore di zero.");
        }

        if (amount > balance) {
            throw new IllegalArgumentException("Saldo insufficiente.");
        }

        // Modifica: Controlla se la somma dell'importo da pagare e di quanto già speso oggi supera il limite giornaliero
        if (spentToday + amount > dailyLimit) {
            throw new IllegalArgumentException("Limite giornaliero superato.");
        }

        balance -= amount;
        spentToday += amount;
        return balance;
    }

    public double getBalance() {
        return balance;
    }

    public double getSpentToday() {
        return spentToday;
    }
}