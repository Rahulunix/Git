def prime_num(num):
    for i in range(2,num):
        if num % i == 0:
            return "not a prime" 
            break
    else:
        return "prime"
    
print(prime_num(769))