a = float(input("請輸入里程數:"))
i=int("70")
x=int("30")
if a>1:
       a=(a-1)*x + i
       print(a)
elif a == 1:
     print(i)
elif 0<a<1:
    a=a*x + i
    print(a)
else:
    print("里程輸入錯誤!")     