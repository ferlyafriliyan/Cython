import os

if __name__ == '__main__':
	try:
		os.system("clear")
		__import__("main").mainx()
	except (KeyboardInterrupt,  Exception) as Error:
		exit("\nErorr Running: {}".format(Error))