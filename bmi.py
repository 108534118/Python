身高=int(input("輸入身高(公分)："))
體重=int(input("輸入體重："))
身高公尺=身高/100
bmi=round(體重/(身高公尺*身高公尺),2)

print("你的BMI為"+str(bmi))

