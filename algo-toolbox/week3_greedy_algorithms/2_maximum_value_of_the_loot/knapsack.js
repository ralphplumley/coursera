// # While Knapsack is not full
//   # Choose item i w/ maximum vi / wi

//   # If item fits into knapsack, take all of it
//   # Otherwise, take so much as to fill the knapsack

// # Return total value and amounts taken

// # backpack = 9lbs max
// # saffron $5000 | 4 lbs
// # vanilla $200 | 3 lbs
// # cinnamon $10 | 5 lbs

// #input: 3 9 5000 4 200 3 10 5

let capacity = 50;

let values = [60, 100, 120];
let weights = [20, 50, 30];

let knapsack = function(capacity, weights, values) {
  totalValue = 0;
  // debugger;
  while (capacity > 0) {

    let bestValue = 0;
    let bestValueIndex;
    for (var i = 0; i < weights.length; i++) {
      let currentValue = values[i]/weights[i];
      if (weights[i] > 0 && (currentValue > bestValue)) {
        bestValue = currentValue;
        bestValueIndex = i;
      }
    }

    if (weights[bestValueIndex] < capacity) {
      totalValue += (bestValue * weights[bestValueIndex]);
      capacity -= weights[bestValueIndex];
      weights[bestValueIndex] -= weights[bestValueIndex];
    } else {
      let amountToTake = weights[bestValueIndex] - capacity;
      totalValue += (bestValue * (capacity - amountToTake));
      weights[bestValueIndex] - amountToTake;
      capacity -= amountToTake;
    }

  }

  return totalValue;
}

console.log(knapsack(capacity, weights, values));