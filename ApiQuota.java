public class ApiQuota {
    private int dailyQuota;
    private int usedToday;

    public ApiQuota(int dailyQuota) {
        this.dailyQuota = dailyQuota;
        this.usedToday = 0;
    }

    public int consume(int units) {
        if (units <= 0) {
            throw new IllegalArgumentException("Le unita devono essere maggiori di zero.");
        }

        if (units > dailyQuota) {
            throw new IllegalArgumentException("Quota giornaliera superata.");
        }

        usedToday += units;
        return usedToday;
    }

    public int getUsedToday() {
        return usedToday;
    }
}
