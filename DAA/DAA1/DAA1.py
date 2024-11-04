# Fibonacci Calculator: Non-Recursive and Recursive Implementations

def fibonacci_recursive(n):
    """
    Calculate Fibonacci number using recursion.
    Time Complexity: O(2^n) - Each call to fibonacci_recursive results in two further calls,
                      leading to an exponential growth of calls.
    Space Complexity: O(n) - The maximum depth of the recursion stack can go up to n.
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_non_recursive(n):
    """
    Calculate Fibonacci number using iteration (non-recursive method).
    Time Complexity: O(n) - The function iterates through all numbers from 2 to n,
                      performing constant time operations.
    Space Complexity: O(1) - Only a fixed number of variables are used, regardless of n.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Test the functions
if __name__ == "__main__":
    n = int(input("Enter a non-negative integer to compute the Fibonacci number: "))

    # Testing Recursive Implementation
    print(f"Fibonacci number (Recursive) for n={n}: {fibonacci_recursive(n)}")

    # Testing Non-Recursive Implementation
    print(f"Fibonacci number (Non-Recursive) for n={n}: {fibonacci_non_recursive(n)}")

    # Analyze performance for larger values
    import time

    # Measure the time taken for recursive implementation
    start_time = time.time()
    print(f"Fibonacci number (Recursive) for n={n}: {fibonacci_recursive(n)}")
    print(f"Time taken (Recursive): {time.time() - start_time:.5f} seconds")

    # Measure the time taken for non-recursive implementation
    start_time = time.time()
    print(f"Fibonacci number (Non-Recursive) for n={n}: {fibonacci_non_recursive(n)}")
    print(f"Time taken (Non-Recursive): {time.time() - start_time:.5f} seconds")
