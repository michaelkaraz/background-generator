import sys
def is_prime(x):  
    if x < 2:  
        return False  
    for n in range(2, (x)-1):  
        if x % n == 0:  
            return False  
    return True

def main(x):
    is_prime(x)

if(__name__ == '__main__'):
    main(sys.argv[1])