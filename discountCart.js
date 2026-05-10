class DiscountCart {
    constructor(maxDiscount = 50) {
        this.maxDiscount = maxDiscount;
        this.discountUsed = 0;
    }

    applyDiscount(amount) {
        if (amount <= 0) {
            throw new Error("Lo sconto deve essere maggiore di zero.");
        }

        // Verifica se l'importo dello sconto da applicare, sommato allo sconto già utilizzato, supera il massimo consentito.
        if (this.discountUsed + amount > this.maxDiscount) {
            throw new Error("Sconto massimo superato.");
        }

        this.discountUsed += amount;
        return this.discountUsed;
    }
}

module.exports = DiscountCart;