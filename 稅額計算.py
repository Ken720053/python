tax=int(input("請輸入今年收入淨額:"))
if(tax>2000000):
    print("付稅金額:",tax*0.3)
elif(1000000<=tax<=1999999):
    print("付稅金額:",tax*0.21)
elif(600000<=tax<=999999):
    print("付稅金額:",tax*0.13)
elif(300000<=tax<=599999):
    print("付稅金額:",tax*0.6)
else:
    print("付稅金額:免稅")