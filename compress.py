import brotli

# Compress data
data_to_compress = b"This is some data to be compressed using Brotli."
compressed_data = brotli.compress(data_to_compress)

# Decompress data
decompressed_data = brotli.decompress(compressed_data)

print("Original data:", data_to_compress)
print("Compressed data:", compressed_data)
print("Decompressed data:", decompressed_data)