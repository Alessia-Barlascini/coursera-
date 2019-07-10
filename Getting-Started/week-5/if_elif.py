# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
score = float(input("Enter Score: "))
if score >= 0.9:
	print ("A")
elif score >= 0.8:
	print ("B")
elif score >= 0.7:
	print ("C")
elif score >= 0.6:
	print ("D")
elif score < 0.6:
	print ("F")
else:
    print ("the entered score is not valid")