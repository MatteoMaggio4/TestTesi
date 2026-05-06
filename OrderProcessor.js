const CartManager = require('./CartManager');
const DiscountService = require('./DiscountService');

class OrderProcessor {
    constructor() {
        this.cartManager = new CartManager();
        this.discountService = new DiscountService();
        this.walletBalance = 100.0;
    }

    addToOrder(productName, price, quantity) {
        return this.cartManager.addItem(productName, price, quantity);
    }

    checkout(couponCode = null) {
        if (this.cartManager.isEmpty()) {
            return { status: "FAILED", message: "Cart is empty" };
        }

        let total = this.cartManager.calculateTotal();
        let totalItems = this.cartManager.cart.reduce((sum, item) => sum + item.quantity, 0);

        total = this.discountService.applyBulkDiscount(total, totalItems);

        if (couponCode) {
            total = this.discountService.applyCoupon(total, couponCode);
        }

        // Assicuriamoci che il total non diventi negativo a causa di sconti eccessivi prima di confrontarlo con il wallet
        if (total < 0) {
            total = 0;
        }

        if (this.walletBalance >= total) {
            // Assumendo che il checkout "consumi" il saldo del wallet,
            // ma il codice fornito non implementa questa logica.
            // Per ora, restituiamo semplicemente lo stato di successo.
            // Se fosse necessario aggiornare this.walletBalance:
            // this.walletBalance -= total;
            return { status: "SUCCESS", finalTotal: total, remainingBalance: this.walletBalance };
        } else {
            return { status: "FAILED", message: "Insufficient funds" };
        }
    }
}

module.exports = OrderProcessor;