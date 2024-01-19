import hmac
import hashlib
import time

# Define the shared secret (replace with your user ID)
userid = "avinashgund95@gmail.com"
shared_secret = userid + "HENNGECHALLENGE003"

# Define constants
time_step = 30
T0 = 0
hash_algorithm = hashlib.sha512
output_digits = 6

# Calculate the current time in terms of time step
current_time = int(time.time()) // time_step

# Convert the shared secret to bytes
shared_secret_bytes = shared_secret.encode('utf-8')

# Create a byte array representing the current time
time_bytes = current_time.to_bytes((current_time.bit_length() + 7) // 8, byteorder='big')

# Calculate the HMAC-SHA-512 hash
hmac_hash = hmac.new(shared_secret_bytes, time_bytes, hash_algorithm).digest()

# Extract the 4-byte dynamic binary code (DT)
offset = hmac_hash[-1] & 0x0F
dt = (hmac_hash[offset] & 0x7F) << 24 | (hmac_hash[offset + 1] & 0xFF) << 16 | (hmac_hash[offset + 2] & 0xFF) << 8 | (hmac_hash[offset + 3] & 0xFF)

# Apply modulo and format as a 6-digit code
otp = dt % 10**output_digits

# Print the generated TOTP
print(f"TOTP: {otp:06d}")
