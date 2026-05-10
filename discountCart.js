class DiscountCart {
    constructor(maxDiscount = 50) {
        this.maxDiscount = maxDiscount;
        this.discountUsed = 0;
    }

    applyDiscount(amount) {
        if (amount <= 0) {
            throw new Error("Lo sconto deve essere maggiore di zero.");
        }

        if (amount > this.maxDiscount) {
            throw new Error("Sconto massimo superato.");
        }

        this.discountUsed += amount;
        return this.discountUsed;
    }
}

module.exports = DiscountCart;
