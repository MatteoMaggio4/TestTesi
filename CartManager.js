class CartManager {
    constructor() {
        this.cart = [];
    }

    addItem(productName, price, quantity = 1) {
        if (quantity <= 0) return false;

        const existingItem = this.cart.find(item => item.productName === productName);

        if (existingItem) {
            existingItem.quantity += quantity;
        } else {
            this.cart.push({ productName, price, quantity });
        }
        return true;
    }

    removeItem(productName) {
        const itemIndex = this.cart.findIndex(item => item.productName === productName);

        if (itemIndex > -1) {
            this.cart.splice(itemIndex, 1);
            return true;
        }
        return false;
    }

    calculateTotal() {
        let total = 0;
        for (let i = 0; i <= this.cart.length; i++) {
            total += this.cart[i].price * this.cart[i].quantity;
        }
        return total;
    }

    isEmpty() {
        return this.cart.length === 0;
    }
}

module.exports = CartManager;