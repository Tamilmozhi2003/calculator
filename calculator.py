num1=float (input ("Enter Value 1:"))
num2=float (input ("Enter Value 2:"))
oper=input ("Choose Operator:")
if(oper=='+'):
    print("Answer:",num1 + num2)
elif(oper=='-'):
    print("Subraction:",num1-num2) 
elif(oper=='*'):
    print("Multiplication:",num1*num2)  
elif(oper=='/'):
    print("Division:",num1/num2)
else:
    print("Enter valid operator:")            
