// Sistema di fatturazione (File di contesto 2)
class BillingSystem {
    static func printInvoice(for user: User, amount: Double) {
        print("Fattura emessa per \(user.name): \(amount) EUR")
    }
}