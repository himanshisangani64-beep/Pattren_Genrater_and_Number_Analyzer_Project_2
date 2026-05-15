while True:
    print("Welcome To The Pattern Genrater And Number Analyzer ")
    print("-----Menu-----")
    print("1) Genrate A Pattern")
    print("2) Analyze a Range Of Number")
    print("3) Exit")
    print(" ")
    ch = int(input("Enter Your Choice "))
    match ch:
        case 1 :
            num = int(input("Enter A number"))
            for i in range(0,num+1):
                for j in range(1,i+1):
                    print("*",end=" ")
                print(" ") 


            print(" ")    
        case 2 :
            t = 0
            num1 = int(input("Enter First Number"))
            num2 = int(input("Enter Second Number"))

            print(" ")

            for i in range(num1,num2):
                if i%2==0:
                    print("Even Number",i)
                    
                else:
                    print("odd Number",i)
                t+=i 
            print(f"All Element Sum from {num1} to  {num2} is :     {t} \n ")
            print(" ")
        case 3:

            print("Exit The Program Good By\n ")

            break            