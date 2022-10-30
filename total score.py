stn1=str(input("請輸入第一位學生姓名:"))
score1=int(input("請輸入第一位學生成績:"))
stn2=str(input("請輸入第二位學生姓名:"))
score2=int(input("請輸入第二位學生成績:"))

Total = int(score1 + score2)

print("姓名  成績")
print(str(stn1) , int(score1))
print(str(stn2) , int(score2))
print("成績總分為:" ,Total)