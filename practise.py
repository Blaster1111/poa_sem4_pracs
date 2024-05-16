def twoscomplement(num):
    onesC = ""
    for i in num:
        if i=="1":
            onesC+="0"
        else:
            onesC+="1"
    return bin(int(onesC,2)+int("1",2)).replace("0b","")


num1 = int(input("Enter first number"))
num2 = int(input("Enter second number:"))

bin1 = bin(abs(num1)).replace("0b","")
bin2 = bin(abs(num2)).replace("0b","")

maxlen = len(bin1)
bin1 = bin1.zfill(maxlen)
bin2 = bin2.zfill(maxlen+1)

binC2 = twoscomplement(bin2)
binC2 = binC2.zfill(maxlen)

print("Iteration   A         Q")
count = maxlen
a=""
a = a.zfill(maxlen+1)
leftshift = ""
m = bin2
minusm = binC2
q = bin1

while count>0:
    merged = a+q
    leftshift = merged[1:]
    a = leftshift[:maxlen+1]

    if a[0]=="1":
        a = bin(int(a,2)+int(m,2)).replace("0b","")
        if len(a)>maxlen+1:
            a = a[1:]
        a = a.zfill(maxlen+1)
    else:
        a = bin(int(a,2)+int(minusm,2)).replace("0b","")
        if len(a)>maxlen+1:
            a = a[1:]
        a = a.zfill(maxlen+1)

    leftshift = a+q[1:]

    if a[0]=="1":
        leftshift+="0"
    else:
        leftshift+="1"

    a = leftshift[:maxlen+1]
    q = leftshift[maxlen+1:]
    count-=1
    print(maxlen - count, a, q)

if a[0]=="1":
    a = bin(int(a,2)+int(m,2)).replace("0b","")
    if len(a)>maxlen+1:
        a = a[1:]

print(int(a, 2))
print(int(q, 2))