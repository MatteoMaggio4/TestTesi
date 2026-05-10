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

        // BUG: checks only the current assignment, not the amount already used.
        if (points > this.maxBudget) {
            throw new Error("Reward budget exceeded.");
        }

        this.usedBudget += points;
        return this.usedBudget;
    }
}

module.exports = RewardBudget;
