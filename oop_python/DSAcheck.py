
def calFact(n):
    fact = 1
    i=1
    def factorial():
        nonlocal fact,i
        if i>n:
             return
        fact*=i
        i+=1
        factorial()
    factorial()
    return fact

          
def fizzBuzz():
    for i in range(1,100):
        
        if(i%3 ==0 and i%5 == 0):
            print("Fizz Buzz \n")
        elif i%3 == 0:
            print("fizz \n")
        elif(i%5 == 0):
            print("Buzz \n")
        else:
            print(f"{i}\n")
fizzBuzz()
