async function simulateNetwork(payment) {
    return new Promise(resolve => setTimeout(resolve, 100));
}

async function processAllPayments(payments) {
    let processedCount = 0;
    
    // Il bug è qui: forEach non "aspetta" le callback asincrone
    payments.forEach(async (p) => {
        await simulateNetwork(p);
        processedCount++;
    });
    
    // Ritorna sempre 0 perché il loop non si è bloccato
    return processedCount; 
}
// Test del codice
processAllPayments([10, 20, 30]).then(res => console.log("Processati:", res));
//riprovo seconda volta
