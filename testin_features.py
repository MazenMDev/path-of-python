def is_strong(password):
    if len(password) >= 8:
        return True
    else:
        return False

# Test some passwords
passwords = ["1234", "password", "goodpass123"]

for p in passwords:
    if is_strong(p):
        print(p, "is strong 💪")
    else:
        print(p, "is weak ❌")
