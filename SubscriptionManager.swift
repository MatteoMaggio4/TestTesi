
class SubscriptionManager {
    
    static func calculateFee(user: User, basePrice: Double) -> Double {
        if user.isPremium {
            let discount = 0.20
            return basePrice * discount 
        }
        return basePrice
    }
}// SubscriptionManager si occupa di calcolare la tariffa per un utente, applicando uno sconto se l'utente è premium.