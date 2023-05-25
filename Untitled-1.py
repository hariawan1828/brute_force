def sieve_of_eratosthenes(n):
    # Inisialisasi array semua bilangan dengan nilai True
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    # Saring bilangan non-prima menggunakan algoritma Sieve of Eratosthenes
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    # Membuat daftar bilangan prima
    prime_numbers = [num for num, is_prime in enumerate(primes) if is_prime]

    return prime_numbers


# Contoh penggunaan
n = 100
prime_numbers = sieve_of_eratosthenes(n)
print("Bilangan prima antara 1 dan", n, "adalah:")
print(prime_numbers
