import string

# Step 1: Asking the user for a password
password = input("Enter a password: ")

# Step 2: Initializing criteria flags and score
length_ok = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in string.punctuation for char in password)

# Tracking what the password is missing
missing = []

if not length_ok:
    missing.append("at least 8 characters")
if not has_upper:
    missing.append("one uppercase letter")
if not has_lower:
    missing.append("one lowercase letter")
if not has_digit:
    missing.append("one digit")
if not has_special:
    missing.append("one special character (e.g., @, #, $)")

# Step 3: Display result
if not missing:
    print("✅ Your password is strong! 💪")
else:
    print("❌ Your password needs:", ", ".join(missing) + ".")

# 🔥 Bonus: Password Strength Meter (Score out of 10)
score = 0
if length_ok: score += 2
if has_upper: score += 2
if has_lower: score += 2
if has_digit: score += 2
if has_special: score += 2

print(f"🔒 Password Strength Score: {score}/10")

if score < 6:
    print("⚠️ Weak password. Try adding more complexity.")
elif score < 10:
    print("👍 Decent password. Almost there!")
else:
    print("🏆 Perfect score! Your password rocks!")
