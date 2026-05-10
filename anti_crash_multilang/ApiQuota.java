public class ApiQuota {
    /*
     * Java API quota module.
     * It uses the same cumulative rule described in sharedPolicy.ts.
     */
    private final int dailyLimit;
    private int usedToday;

    public ApiQuota(int dailyLimit) {
        this.dailyLimit = dailyLimit;
        this.usedToday = 0;
    }

    public int consume(int units) {
        if (units <= 0) {
            throw new IllegalArgumentException("Units must be greater than zero.");
        }

        // BUG: checks only the current request, not usedToday + units.
        if (units > dailyLimit) {
            throw new IllegalArgumentException("Daily quota exceeded.");
        }

        usedToday += units;
        return usedToday;
    }

    public int getUsedToday() {
        return usedToday;
    }
}
