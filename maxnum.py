numa = int(input("請輸入a的值:"))
numb = int(input("請輸入b的值:"))
numc = int(input("請輸入c的值:"))

if(numa>numb>numc):
    print("最大值為:"+str(numa))
elif(numb>numa>numc):
    print("最大值為:"+str(numa))
elif(numb>numa>numc):
    print("最大值為:"+str(numb))
elif(numb>numc>numa):
    print("最大值為:"+str(numb))
elif(numc>numb>numa):
    print("最大值為:"+str(numc))   
elif(numc>numa>numb):
    print("最大值為:"+str(numc))