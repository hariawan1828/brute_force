import itertools

def brute_force():
    password = input("Masukkan kata sandi numerik 4 digit: ")
    chars = "0123456789"
    attempts = 0

    for password_length in range(1, 5):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                print(f"Kata sandi ditemukan setelah {attempts} percobaan.")
                return
    print("Kata sandi tidak ditemukan.")
    brute_force()

brute_force()
