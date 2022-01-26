# BigData_HW3

hour   = float(input("시간 : "))
minute = float(input("분 : "))

if (hour < 1) | (hour > 12):
	hour = 6

angle = hour*30 + minute*0.5

if angle >360:
	angle = angle%360

print("시침이 이동한 각도 : ",angle)