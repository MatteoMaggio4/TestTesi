List<int> filterPositives(List<int> numbers) {
  // Crea una copia per non modificare l'originale
  List<int> result = List.from(numbers);
  
  // BUG: Rimuovere elementi durante un ciclo for progressivo
  // causa il salto dell'elemento successivo a quello rimosso.
  for (int i = 0; i < result.length; i++) {
    if (result[i] < 0) {
      result.removeAt(i);
    }
  }
  
  return result;
}

void main() {
  // Test Case critico: ci sono due numeri negativi vicini (-5, -2)
  // Il sistema fallirà e restituirà [10, -2, 8] invece di [10, 8]
  var data = [10, -5, -2, 8, -1];
  print("Lista filtrata: ${filterPositives(data)}");
}