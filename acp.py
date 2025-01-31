def calcuBill(g,b):
    remain=g-b
    
    if remain>0:
        print(f"Return amount: {remain}")
    elif remain==0:
        print("Exact amount given, no change need man.")
    
    
    
g=int(input("Enter the  given amount: "))
b=int(input("Enter the bill amount: "))

calcuBill(g,b)
