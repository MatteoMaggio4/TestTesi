class RewardBudget {
    constructor(maxBudget = 100) {
        this.maxBudget = maxBudget;
        this.usedBudget = 0;
    }

    assign(points) {
        if (points <= 0) {
            throw new Error("I punti devono essere maggiori di zero.");
        }

        if (points > this.maxBudget) {
            throw new Error("Budget premi superato.");
        }

        this.usedBudget += points;
        return this.usedBudget;
    }
}

module.exports = RewardBudget;
