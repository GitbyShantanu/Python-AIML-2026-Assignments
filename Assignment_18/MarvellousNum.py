# (for Ass18_Q5)
# Module : MarvellousNum 

def ChkPrime(No):
    for i in range(2, No//2 + 1):
        if No % i == 0:
            return False
    
    return True