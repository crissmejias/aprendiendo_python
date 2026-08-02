def es_par(n):
    return True if n % 2 == 0 else False
    
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    print(es_par(5))
    print(factorial(5))