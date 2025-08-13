import math
import cmath
import statistics
import numpy as np
from sympy import symbols, Eq, solve, simplify, diff, integrate, limit, sin, cos, tan, log, exp, sqrt, pi

class AdvancedCalculator:
    def __init__(self):
        self.history = []
        self.memory = 0
    
    def add_to_history(self, operation, result):
        entry = f"{operation} = {result}"
        self.history.append(entry)
        return entry
    
    def basic_operations(self, expression):
        """Evaluate basic arithmetic expressions"""
        try:
            result = eval(expression, {'__builtins__': None}, 
                         {'math': math, 'cmath': cmath, 'np': np, 'pi': math.pi, 'e': math.e})
            self.add_to_history(expression, result)
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    def solve_equation(self, equation_str, variable='x'):
        """Solve algebraic equations"""
        try:
            x = symbols(variable)
            equation = Eq(eval(equation_str.split('=')[0], {'__builtins__': None}, 
                          {'x': x, 'math': math, 'sin': sin, 'cos': cos, 'tan': tan, 
                           'log': log, 'exp': exp, 'sqrt': sqrt, 'pi': pi}),
                          eval(equation_str.split('=')[1], {'__builtins__': None}, 
                          {'x': x, 'math': math, 'sin': sin, 'cos': cos, 'tan': tan, 
                           'log': log, 'exp': exp, 'sqrt': sqrt, 'pi': pi}))
            solutions = solve(equation, x)
            self.add_to_history(f"Solve {equation_str} for {variable}", solutions)
            return solutions
        except Exception as e:
            return f"Error: {str(e)}"
    
    def calculate_derivative(self, expression_str, variable='x', point=None):
        """Calculate derivative of a function"""
        try:
            x = symbols(variable)
            expr = eval(expression_str, {'__builtins__': None}, 
                       {'x': x, 'math': math, 'sin': sin, 'cos': cos, 'tan': tan, 
                        'log': log, 'exp': exp, 'sqrt': sqrt, 'pi': pi})
            derivative = diff(expr, x)
            
            if point is not None:
                value = derivative.subs(x, point)
                result = f"Derivative: {derivative}, Value at {variable}={point}: {value}"
            else:
                result = derivative
                
            self.add_to_history(f"Derivative of {expression_str}", result)
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    def calculate_integral(self, expression_str, variable='x', limits=None):
        """Calculate definite or indefinite integral"""
        try:
            x = symbols(variable)
            expr = eval(expression_str, {'__builtins__': None}, 
                       {'x': x, 'math': math, 'sin': sin, 'cos': cos, 'tan': tan, 
                        'log': log, 'exp': exp, 'sqrt': sqrt, 'pi': pi})
            
            if limits:
                a, b = limits
                integral = integrate(expr, (x, a, b))
                result = f"Integral from {a} to {b}: {integral}"
            else:
                integral = integrate(expr, x)
                result = f"Indefinite integral: {integral}"
                
            self.add_to_history(f"Integral of {expression_str} {f'from {limits[0]} to {limits[1]}' if limits else ''}", result)
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    def calculate_limit(self, expression_str, variable='x', approach="0", direction="+"):
        """Calculate limit of a function"""
        try:
            x = symbols(variable)
            expr = eval(expression_str, {'__builtins__': None}, 
                       {'x': x, 'math': math, 'sin': sin, 'cos': cos, 'tan': tan, 
                        'log': log, 'exp': exp, 'sqrt': sqrt, 'pi': pi})
            
            approach_point = eval(approach, {'__builtins__': None}, {'math': math, 'pi': pi, 'e': math.e})
            
            if direction == "+":
                lim = limit(expr, x, approach_point, '+')
            elif direction == "-":
                lim = limit(expr, x, approach_point, '-')
            else:
                lim = limit(expr, x, approach_point)
                
            result = f"Limit of {expression_str} as {variable}→{approach}{direction if direction in '+-' else ''}: {lim}"
            self.add_to_history(result, "")
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    def matrix_operations(self, operation, matrix1, matrix2=None):
        """Perform matrix operations"""
        try:
            if operation == "add":
                result = np.add(matrix1, matrix2)
            elif operation == "subtract":
                result = np.subtract(matrix1, matrix2)
            elif operation == "multiply":
                result = np.matmul(matrix1, matrix2)
            elif operation == "determinant":
                result = np.linalg.det(matrix1)
            elif operation == "inverse":
                result = np.linalg.inv(matrix1)
            elif operation == "transpose":
                result = np.transpose(matrix1)
            else:
                return "Invalid matrix operation"
            
            self.add_to_history(f"Matrix {operation}", result)
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    def statistical_calculations(self, data, operation):
        """Perform statistical operations"""
        try:
            if operation == "mean":
                result = statistics.mean(data)
            elif operation == "median":
                result = statistics.median(data)
            elif operation == "mode":
                result = statistics.mode(data)
            elif operation == "stdev":
                result = statistics.stdev(data)
            elif operation == "variance":
                result = statistics.variance(data)
            else:
                return "Invalid statistical operation"
            
            self.add_to_history(f"Statistical {operation} of {data}", result)
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    def memory_store(self, value):
        """Store a value in memory"""
        self.memory = value
        return f"Memory stored: {value}"
    
    def memory_recall(self):
        """Recall value from memory"""
        return self.memory
    
    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
        return "Memory cleared"
    
    def show_history(self):
        """Display calculation history"""
        return "\n".join(self.history) if self.history else "No history available"
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = []
        return "History cleared"


def main():
    calc = AdvancedCalculator()
    print("Advanced Calculator")
    print("Available operations:")
    print("1. Basic arithmetic (+, -, *, /, ^)")
    print("2. Algebraic equation solving")
    print("3. Derivatives")
    print("4. Integrals")
    print("5. Limits")
    print("6. Matrix operations")
    print("7. Statistical calculations")
    print("8. Memory functions")
    print("9. View history")
    print("0. Exit")
    
    while True:
        choice = input("\nEnter your choice (0-9): ")
        
        if choice == '0':
            print("Exiting calculator...")
            break
            
        elif choice == '1':
            expr = input("Enter arithmetic expression (e.g., 2+3*5, sin(pi/2), log(100)): ")
            print("Result:", calc.basic_operations(expr))
            
        elif choice == '2':
            eq = input("Enter equation to solve (e.g., x**2 - 4 = 0): ")
            var = input("Enter variable (default 'x'): ") or 'x'
            print("Solutions:", calc.solve_equation(eq, var))
            
        elif choice == '3':
            expr = input("Enter function expression (e.g., x**2 + 3*x): ")
            var = input("Enter variable (default 'x'): ") or 'x'
            point = input("Optional: evaluate at point (leave blank for general derivative): ")
            point = float(point) if point else None
            print("Result:", calc.calculate_derivative(expr, var, point))
            
        elif choice == '4':
            expr = input("Enter function to integrate (e.g., x**2 + 3*x): ")
            var = input("Enter variable (default 'x'): ") or 'x'
            limits_input = input("Optional: enter limits as 'a,b' (leave blank for indefinite): ")
            limits = tuple(map(float, limits_input.split(','))) if limits_input else None
            print("Result:", calc.calculate_integral(expr, var, limits))
            
        elif choice == '5':
            expr = input("Enter function for limit (e.g., sin(x)/x): ")
            var = input("Enter variable (default 'x'): ") or 'x'
            approach = input("Enter approach point (default '0'): ") or "0"
            direction = input("Enter direction (+ or -, leave blank for two-sided): ") or ""
            print("Result:", calc.calculate_limit(expr, var, approach, direction))
            
        elif choice == '6':
            print("Matrix operations: add, subtract, multiply, determinent, inverse, transpose")
            op = input("Enter operation: ")
            rows = int(input("Enter number of rows for matrix 1: "))
            cols = int(input("Enter number of columns for matrix 1: "))
            print("Enter matrix 1 elements row-wise (space separated):")
            elements = list(map(float, input().split()))
            matrix1 = np.array(elements).reshape(rows, cols)
            
            matrix2 = None
            if op in ["add", "subtract", "multiply"]:
                rows2 = int(input("Enter number of rows for matrix 2: "))
                cols2 = int(input("Enter number of columns for matrix 2: "))
                print("Enter matrix 2 elements row-wise (space separated):")
                elements2 = list(map(float, input().split()))
                matrix2 = np.array(elements2).reshape(rows2, cols2)
            
            print("Result:", calc.matrix_operations(op, matrix1, matrix2))
            
        elif choice == '7':
            data = list(map(float, input("Enter data points separated by spaces: ").split()))
            op = input("Enter operation (mean, median, mode, stdev, variance): ")
            print("Result:", calc.statistical_calculations(data, op))
            
        elif choice == '8':
            mem_op = input("Memory operation (store, recall, clear): ")
            if mem_op == "store":
                value = float(input("Enter value to store: "))
                print(calc.memory_store(value))
            elif mem_op == "recall":
                print("Memory value:", calc.memory_recall())
            elif mem_op == "clear":
                print(calc.memory_clear())
            else:
                print("Invalid memory operation")
                
        elif choice == '9':
            print("\nCalculation History:")
            print(calc.show_history())
            if input("Clear history? (y/n): ").lower() == 'y':
                print(calc.clear_history())
                
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()