List<int> filterPositives(List<int> numbers) {

  List<int> result = List.from(numbers);
  
  for (int i = 0; i < result.length; i++) {
    if (result[i] < 0) {
      result.removeAt(i);
    }
  }
  
  return result;
}

void main() {
  var data = [10, -5, -2, 8, -1];
  print("Lista filtrata: ${filterPositives(data)}");
}