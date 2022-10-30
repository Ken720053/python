a=int(input("請輸入a的值:"))
b=int(input("請輸入b的值:"))
max=(a+1)*(b+1)
for i in range(1,max):
    if(i%a==0 and i%b==0):
        break
print("%d 和 %d 的最小公倍數=%d" %(a,b,i))