# Advanced High-Level Calculator

## Overview
This is a comprehensive Python calculator that can handle various types of mathematical problems, including arithmetic, algebraic, trigonometric, logarithmic, calculus, matrix operations, and statistical calculations. The calculator features memory functions and maintains a history of all calculations.

## Features
- **Basic Arithmetic**: Standard operations (+, -, *, /, ^) with proper order of operations
- **Scientific Functions**: Trigonometric, logarithmic, exponential functions
- **Equation Solving**: Solves algebraic equations (linear, quadratic, etc.)
- **Calculus Operations**:
  - Derivatives (symbolic and at specific points)
  - Integrals (definite and indefinite)
  - Limits (including one-sided limits)
- **Matrix Operations**: Addition, subtraction, multiplication, determinant, inverse, transpose
- **Statistical Calculations**: Mean, median, mode, standard deviation, variance
- **Memory Functions**: Store, recall, and clear values
- **History Tracking**: Keeps record of all calculations
- **Complex Numbers**: Supports complex number operations

## Requirements
- Python 3.x
- numpy (`pip install numpy`)
- sympy (`pip install sympy`)

## Installation
1. Clone the repository or download the calculator.py file
2. Install the required dependencies:
   ```
   pip install numpy sympy
   ```

## Usage
Run the calculator by executing the Python script:
```
python calculator.py
```

### Menu Options
1. **Basic arithmetic**: Enter arithmetic expressions (e.g., `2+3*5`, `sin(pi/2)`, `log(100)`)
2. **Algebraic equation solving**: Solve equations (e.g., `x**2 - 4 = 0`)
3. **Derivatives**: Calculate derivatives of functions (e.g., `x**2 + 3*x`)
4. **Integrals**: Calculate definite or indefinite integrals
5. **Limits**: Calculate limits of functions
6. **Matrix operations**: Perform matrix calculations (add, subtract, multiply, determinant, inverse, transpose)
7. **Statistical calculations**: Compute mean, median, mode, standard deviation, variance
8. **Memory functions**: Store, recall, and clear values in memory
9. **View history**: Display or clear calculation history
0. **Exit**: Quit the calculator

## Examples
1. Basic arithmetic: `(2+3)*4^2` → 80.0
2. Equation solving: `x**2 - 4 = 0` → [-2, 2]
3. Derivative: `x**2 + 3*x` → 2*x + 3
4. Integral: `x**2` from 0 to 2 → 8/3
5. Limit: `sin(x)/x` as x→0 → 1
6. Matrix multiplication: Multiply two 2x2 matrices
7. Statistics: Calculate mean of [1, 2, 3, 4, 5] → 3.0

## License
This project is open-source and available under the MIT License.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.