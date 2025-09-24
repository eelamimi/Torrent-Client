from typing import Final

from src.app.core.parser.bencoder import Bencoder

# считываем
with open("../../samples/sample.torrent", "rb") as f:
    data = f.read()

print(data)

# убираем BOM
if data.startswith(b'\xef\xbb\xbf'):
    data = data[3:]

bencoder: Final[Bencoder] = Bencoder()
print(bencoder.decode_file(data))