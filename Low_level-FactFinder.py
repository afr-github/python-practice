import math

def main():
    fact_res = 0
    print("Input a number, any real number:")
    my_fact = input()

    
    try:
        if isinstance(int(my_fact), int):
            fact = math.factorial(abs(int(my_fact)))
            fact_res = "{:,.2f}".format(fact)
            return fact_res
        
    except ValueError as ve:
        print("Incorrect type of value: error: {}".format(ve))
        main()
    

print(main())
    