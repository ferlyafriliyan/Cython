# Contoh untuk memanggil file yang sudah diobfuscate dengan Cython
import example # Input_file

if __name__ == '__main__':
	try:
		example.main() # Memanggil/untuk menjalankan def yang berfungsi pada file input yang sudah di obfuscate
	except (KeyboardInterrupt, Exception) as e:
		exit(f"[Error] {str(e).capitalize()}!")
