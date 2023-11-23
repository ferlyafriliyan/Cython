def mainx():
	print("Hello world !")
	
if __name__ == '__main__':
	try:
		mainx()
	except (KeyboardInterrupt, Exception) as e:
		exit(f" [ Error : ] {str(e).capitalize()} !")