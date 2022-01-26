# BigData_HW2

def BMI(height, weight):
	bmi = weight/(height*height)
	return bmi

def Check_BMI(bmi):
	if bmi < 18.5:
		return "체중부족"
	elif 18.5 <= bmi <= 22.9:
		return "정상"
	elif 23.0 <= bmi <= 24.9:
		return "과체중"
	else:
		return "비만"

weight = float(input("몸무게를 입력하세요(kg) : "))
height = float(input("키를 입력하세요(m) : "))

print("당신의 bmi지수는 %f 이며" %BMI(height, weight))
print("현재 상태는 %s 입니다."%Check_BMI(BMI(height, weight)))
