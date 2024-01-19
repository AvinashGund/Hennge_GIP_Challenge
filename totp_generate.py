import hmac
import hashlib
import struct
import time

def generate_totp(user_id, time_step=30):
    # Define the shared secret
    shared_secret = user_id + "HENNGECHALLENGE003"
    
    # Calculate the current time step
    current_time = int(time.time())
    time_step_count = current_time // time_step
    
    # Create the HMAC-SHA-512 hash
    key = bytes(shared_secret, 'utf-8')
    msg = struct.pack('>Q', time_step_count)
    h = hmac.new(key, msg, hashlib.sha512)
    h = bytearray(h.digest())
    
    # Extract the 4-byte dynamic binary code (DTBC)
    offset = h[-1] & 0x0F
    dtbc = h[offset:offset+4]
    
    # Calculate the OTP
    otp = struct.unpack('>I', dtbc)[0] % 10**6
    
    # Format the OTP as a 6-digit string with leading zeros
    otp = str(otp).zfill(6)
    
    return otp

# Replace 'your_user_id' with the actual user ID
user_id = 'avinashgund95@gmail.com'
totp = generate_totp(user_id)
print("Generated TOTP:", totp)
