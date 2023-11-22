import setup

if __name__ == '__main__':
	try:
		setup.clear_terminal()
		setup.get_input_file()
	except (KeyboardInterrupt, Exception) as e:
		exit(f"[Error] {str(e).capitalize()}!")
