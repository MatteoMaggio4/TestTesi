class DiscountService {
    constructor() {
        this.activeCoupons = {
            "SAVE20": 0.20,
            "WELCOME10": 0.10,
            "HALFOFF": 0.50
        };
    }

    applyCoupon(totalAmount, couponCode) {
        if (!totalAmount || totalAmount <= 0) {
            return totalAmount;
        }

        let discountRate = 0;

        if (this.activeCoupons[couponCode]) {
            discountRate = this.activeCoupons[couponCode];
        }

        const discountAmount = totalAmount * discountRate;
        let finalPrice = totalAmount - discountAmount;

        if (finalPrice < 0) {
            finalPrice = 0;
        }

        return finalPrice;
    }

    applyBulkDiscount(totalAmount, itemCount) {
        if (itemCount > 20) { // Controllo più restrittivo per primo
            return totalAmount * 0.80;
        } else if (itemCount > 10) {
            return totalAmount * 0.85;
        } else if (itemCount > 5) {
            return totalAmount * 0.90;
        }
        return totalAmount;
    }
}

module.exports = DiscountService;