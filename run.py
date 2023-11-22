import setup

if __name__ == '__main__':
	try:
		example.clear_terminal()
		example.get_input_file()
	except (KeyboardInterrupt, Exception) as e:
		exit(f"[Error] {str(e).capitalize()}!")