import pyotp
import hashlib
import base64

# Define email and secret
email = "ashwathkannan266@gmail.com"
secret = email + "HENNGECHALLENGE003"

# Convert the secret to base32 encoding
secret_bytes = secret.encode('utf-8')
base32_secret = base64.b32encode(secret_bytes).decode('utf-8')

# Create TOTP object with SHA-512
totp = pyotp.TOTP(base32_secret, digits=10, digest=hashlib.sha512, interval=30)

# Generate TOTP
auth_password = totp.now()
print(auth_password)
