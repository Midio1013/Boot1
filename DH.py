import time
tin=0
ings = True
try:
	while True:
		print(" " * tin,end='')
		print("💨💨💨💨")
		time.sleep(0.01)
		if ings:
			tin += 1
			if tin == 20:
				ings = False
		else:
			tin -= 1
			if tin == 0:
				ings = True
except KeyboardInterrupt:
	print("\nEnd!")
	time.sleep(0.14)
	sys.exit()