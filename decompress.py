def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number

p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
compressed_key = "020795da6e3547eb73fac3f2b56c89c34f8e32049bafd0747957219e4c09f37e4c"
y_parity = int(compressed_key[:2]) - 2
x = int(compressed_key[2:], 16)
a = (pow_mod(x, 3, p) + 7) % p
y = pow_mod(a, (p+1)//4, p)
if y % 2 != y_parity:
    y = -y % p
uncompressed_key = '04{:x}{:x}'.format(x, y)

print(uncompressed_key)    # 04 795da6e3547eb73fac3f2b56c89c34f8e32049bafd0747957219e4c09f37e4c 69943eb7f693f5311fb4caa7d63a51f6f5ef20924f642fa8502b553eadc6cb26
