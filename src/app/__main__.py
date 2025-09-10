from src.app.core.parser.bencoder import decode

# считываем
with open("../../samples/alice.torrent", "rb") as f:
    data = f.read()

print(data)

# убираем BOM
if data.startswith(b'\xef\xbb\xbf'):
    data = data[3:]

print(data)
print(ord(b'd'))
# обрабатываем .torrent
decode(data)
