class RewardBudget {
    /*
     * JavaScript reward module.
     * It mirrors the same cumulative rule described in sharedPolicy.ts.
     */
    constructor(maxBudget = 100) {
        this.maxBudget = maxBudget;
        this.usedBudget = 0;
    }

    assign(points) {
        if (points <= 0) {
            throw new Error("Points must be greater than zero.");
        }

        // BUG FIXED: checks the cumulative daily total, not just the current request.
        if (this.usedBudget + points > this.maxBudget) {
            throw new Error("Reward budget exceeded.");
        }

        this.usedBudget += points;
        return this.usedBudget;
    }
}

module.exports = RewardBudget;