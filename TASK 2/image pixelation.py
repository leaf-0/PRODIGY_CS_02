from PIL import Image

def encrypt_image(input_path, output_path, key):
  """Encrypts an image using XOR operation with a key."""
  image = Image.open(input_path)
  width, height = image.size
  pixels = image.load()

  key_list = [ord(char) for char in key] * ((width * height) // len(key) + 1)


  for y in range(height):
    for x in range(width):
      r, g, b = pixels[x, y]
      new_r = r ^ key_list[y * width + x]
      new_g = g ^ key_list[y * width + x]
      new_b = b ^ key_list[y * width + x]
      pixels[x, y] = (new_r, new_g, new_b)

  image.save(output_path)

def decrypt_image(input_path, output_path, key):
  """Decrypts an image using XOR operation with the same key."""
  encrypt_image(input_path, output_path, key)  


input_path = "image.jpg"
output_path = "encrypted_image.jpg"
key = "secret"

encrypt_image(input_path, output_path, key)

decrypted_path = "decrypted_image.jpg"
decrypt_image(output_path, decrypted_path, key)

print(f"Image encrypted to {output_path}")
print(f"Image decrypted to {decrypted_path}")
