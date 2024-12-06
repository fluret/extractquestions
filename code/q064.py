import zlib

s = b"hello world!hello world!hello world!hello world!"
t = zlib.compress(s)
print(t)
t = zlib.decompress(t)
print(t)
