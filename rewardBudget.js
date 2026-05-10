class RewardBudget {
    constructor(maxBudget = 100) {
        this.maxBudget = maxBudget;
        this.usedBudget = 0;
    }

    assign(points) {
        if (points <= 0) {
            throw new Error("I punti devono essere maggiori di zero.");
        }

        // Aggiunto controllo per assicurarsi che l'assegnazione non superi il budget rimanente
        if (this.usedBudget + points > this.maxBudget) {
            throw new Error("Budget premi superato.");
        }

        this.usedBudget += points;
        return this.usedBudget;
    }
}

module.exports = RewardBudget;