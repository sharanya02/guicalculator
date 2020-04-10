import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")

val = ""
A = "0"
operator = ""

def findSum(str1, str2):  
    if (len(str1) > len(str2)): 
        t = str1; 
        str1 = str2; 
        str2 = t;  
    str = "";  
    n1 = len(str1); 
    n2 = len(str2);  
    str1 = str1[::-1];  
    str2 = str2[::-1];  
    carry = 0;  
    for i in range(n1):  
        sum = ((ord(str1[i]) - 48) + ((ord(str2[i]) - 48) + carry));  
        str += chr(sum % 10 + 48);  
        carry = int(sum / 10);  
   
    for i in range(n1, n2):  
        sum = ((ord(str2[i]) - 48) + carry);  
        str += chr(sum % 10 + 48);  
        carry = (int)(sum / 10);  
  
    if (carry):  
        str += chr(carry + 48);  
   
    str = str[::-1];  
    return str;  
    
str1 = "12";  
str2 = "198111";  
print(findSum(str1, str2));  

def isSmaller(str1, str2):  
    n1 = len(str1)  
    n2 = len(str2) 
   
    if (n1 < n2): 
        return True
    if (n2 < n1): 
        return False
   
    for i in range(n1): 
        if (str1[i] < str2[i]): 
            return True
        elif (str1[i] > str2[i]): 
            return False
   
    return False
   
def findDiff(str1, str2): 
    if (isSmaller(str1, str2)): 
        temp = str1 
        str1 = str2 
        str2 = temp 
   
    str3 = "" 
    n1 = len(str1)  
    n2 = len(str2) 
    str1= str1[::-1] 
    str2 = str2[::-1] 
    carry = 0 
    for i in range(n2):      
        sub = ((ord(str1[i])-ord('0'))-(ord(str2[i])-ord('0'))-carry)   
        if (sub < 0): 
            sub = sub + 10
            carry = 1 
        else: 
            carry = 0
        str3 = str3+str(sub ) 
    for i in range(n2,n1): 
        sub = ((ord(str1[i])-ord('0')) - carry) 
        if (sub < 0): 
            sub = sub + 10
            carry = 1
        else: 
            carry = 0     
        str3 = str3+str(sub ) 
    str3= str3[::-1] 
    return str3 
   
if __name__ == "__main__": 
    str1 = "978"
    str2 = "12977"
    print(findDiff(str1, str2))


def multiply(num1, num2): 
    len1 = len(num1) 
    len2 = len(num2) 
    if len1 == 0 or len2 == 0: 
        return "0"
    result = [0] * (len1 + len2) 
    i_n1 = 0
    i_n2 = 0
    for i in range(len1 - 1, -1, -1): 
        carry = 0
        n1 = ord(num1[i]) - 48
        i_n2 = 0
        for j in range(len2 - 1, -1, -1): 
            n2 = ord(num2[j]) - 48 
            summ = n1 * n2 + result[i_n1 + i_n2] + carry  
            carry = summ // 10
            result[i_n1 + i_n2] = summ % 10
            i_n2 += 1
        if (carry > 0): 
            result[i_n1 + i_n2] += carry  
        i_n1 += 1
    i = len(result) - 1
    while (i >= 0 and result[i] == 0): 
        i -= 1
    if (i == -1): 
        return "0"
    s = "" 
    while (i >= 0): 
        s += chr(result[i] + 48) 
        i -= 1
    return s   
str1 = "1235421415454545454545454544"
str2 = "1714546546546545454544548544544545"  
if((str1[0] == '-' or str2[0] == '-') and 
   (str1[0] != '-' or str2[0] != '-')): 
    print("-", end = '')   
if(str1[0] == '-' and str2[0] != '-'): 
    str1 = str1[1:] 
elif(str1[0] != '-' and str2[0] == '-'): 
    str2 = str2[1:] 
elif(str1[0] == '-' and str2[0] == '-'): 
    str1 = str1[1:] 
    str2 = str2[1:] 
print(multiply(str1, str2)) 

import math 
  
def longDivision(number, divisor):  
    ans = "";  
    idx = 0;  
    temp = ord(number[idx]) - ord('0'); 
    while (temp < divisor): 
        temp = (temp * 10 + ord(number[idx + 1]) -
                            ord('0')); 
        idx += 1; 
      
    idx +=1; 
   
    while ((len(number)) > idx):  
          
        # Store result in answer i.e. temp / divisor  
        ans += chr(math.floor(temp // divisor) + ord('0'));  
          
        # Take next digit of number 
        temp = ((temp % divisor) * 10 + ord(number[idx]) -
                                        ord('0')); 
        idx += 1; 
  
    ans += chr(math.floor(temp // divisor) + ord('0')); 
      
  
    if (len(ans) == 0):  
        return "0";  
      
   
    return ans;  
   
number = "1248163264128256512";  
divisor = 125;  
print(longDivision(number, divisor));

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)


# functions for the operator button click
def btn_plus_clicked():
    global A
    global operator,val
    A = val
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_minus_clicked():
    global A
    global operator,val
    A = val
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mult_clicked():
    global A
    global operator,val
    A = val
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_clicked():
    global A
    global operator,val
    A = val
    operator = "/"
    val = val + "/"
    data.set(val)

def btn_c_pressed():
    global A,operator,val
    val = ""
    A = 0
    operator = ""
    data.set(val)


# function to find the result
def result():
    global A,operator,val
    val2 = val
    if operator == "+":
        x = (val2.split("+")[1])
        val = str(findSum(A,x))
        
        data.set(val)
    if operator == "-":
        x = (val2.split("-")[1])
        val = str(findDiff(A,x))
        data.set(val)
    if operator == "*":
        x = (val2.split("*")[1])
        val = str(multiply(A,x))
        data.set(val)
    if operator == "/":
        x = int(val2.split("/")[1])
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            A = ""
            val = ""
            data.set(val)
        else:
            val = str(longDivision(A,x))
            data.set(val)


# the label that shows the result
data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana", 20),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
)
lbl.pack(expand = True, fill = "both")

# the frames section
btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")


# The buttons section
btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_1_isclicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_2_isclicked,
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_3_isclicked,
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btnplus = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_plus_clicked,
)
btnplus.pack(side = LEFT, expand = True, fill = "both",)

# buttons for frame 2

btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_4_isclicked,
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_5_isclicked,
)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_6_isclicked,
)
btn6.pack(side = LEFT, expand = True, fill = "both",)

btnminus = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_minus_clicked,
)
btnminus.pack(side = LEFT, expand = True, fill = "both",)

# button for frame 3

btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_7_isclicked,
)
btn7.pack(side = LEFT, expand = True, fill = "both",)

btn8 = Button(
    btnrow3,
    text = "8",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_8_isclicked,
)
btn8.pack(side = LEFT, expand = True, fill = "both",)

btn9 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_9_isclicked,
)
btn9.pack(side = LEFT, expand = True, fill = "both",)

btnmult = Button(
    btnrow3,
    text = "*",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_mult_clicked,
)
btnmult.pack(side = LEFT, expand = True, fill = "both",)

# button for frame4


btnc = Button(
    btnrow4,
    text = "C",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_c_pressed,
)
btnc.pack(side = LEFT, expand = True, fill = "both",)

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_0_isclicked,
)
btn0.pack(side = LEFT, expand = True, fill = "both",)

btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = result,
)
btnequal.pack(side = LEFT, expand = True, fill = "both",)

btndiv = Button(
    btnrow4,
    text = "/",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_div_clicked,
)
btndiv.pack(side = LEFT, expand = True, fill = "both",)

root.mainloop()

