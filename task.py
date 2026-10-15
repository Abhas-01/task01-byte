import base64

# Challenge Base64 ciphertext
encoded = "QkFJTntiQTczX1E4Ul9BcmhIQ19YNHlHY0R9"

# 1. Decode from Base64
decoded = base64.b64decode(encoded).decode("utf-8")

# 2. Adjust wrapper prefix to the expected BYTE{...} format if required
flag = decoded.replace("BAIN{", "BYTE{")

print("Raw Decoded:   ", decoded)
print("Flag (BYTE format):", flag)

