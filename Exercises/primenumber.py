def prime(num):
    prime_number = 0
    i=2
    while(i<num):
        if(num%i==0):
            prime_number = 1
        i += 1
    if (prime_number == 0):
        print("number ", num, " is prime")
    else:
        print("number ", num ," is not prime")




prime(5)
prime(3)
prime(7)