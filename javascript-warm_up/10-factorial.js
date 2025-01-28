#!/usr/bin/node

// Function to compute factorial recursively
function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

// Retrieve the first argument, cast it to an integer
const arg = parseInt(process.argv[2]);

// Compute and print the factorial
console.log(factorial(arg));
