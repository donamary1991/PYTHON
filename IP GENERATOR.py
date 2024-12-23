# Write a python program to read four numbers (representing the four octets of an IP) and print the next five IP address
# Eg:
# Input:
# 192 168 255 252
# ----------Output---------
# 192 168 255 253
# 192 168 255 254
# 192 168 255 255
# 192 169 0 0
# 192 169 0 1
num1=int(input("enter the octet1"))
num2=int(input("enter the octet2"))
num3=int(input("enter the octet3"))
num4=int(input("enter the octet4"))
if((1<=num1<=255) and ( 0<=num2<=255) and (0<=num3<=255) and (0<=num4<=255)):
 for i in range(1,6):
     num4+=1
     if(num4>255):
        num4=(num4%255)-1
        num3+=1
        if (num3 > 255):
            num3 = (num3 % 255) - 1
            num2 += 1
            if (num2 > 255):
                num2 = (num2 % 255) - 1
                num1 += 1
                if (num1 > 255):
                    print("No more available IP's")
                    break
     print("IP"+str(i)+":"+" "+str(num1) + "." + str(num2) + "." + str(num3) + "." + str(num4))

else:
    print("invalid input")
