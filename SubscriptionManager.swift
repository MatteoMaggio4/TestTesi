// Gestore logica di business (Target File)
class SubscriptionManager {
    
    // BUG LOGICO: Un utente premium dovrebbe avere il 20% di sconto.
    // L'algoritmo invece moltiplica il prezzo per 0.20, facendo pagare SOLO il 20%
    // del totale (es. su 100€, paga 20€ invece di 80€!).
    static func calculateFee(user: User, basePrice: Double) -> Double {
        if user.isPremium {
            let discount = 0.20
            return basePrice * discount // ERRORE GRAVE: dovrebbe essere basePrice * (1.0 - discount) o basePrice - (basePrice * discount)
        }
        return basePrice
    }
}