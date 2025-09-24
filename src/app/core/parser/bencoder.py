class Bencoder:
    def decode_file(self, bencoded_data: bytes):
        ind = 0
        decoded_metadata = []

        while ind < len(bencoded_data):
            char = chr(bencoded_data[ind])
            if char.isdigit():
                string, append_index = self.decode_string(bencoded_data[ind:])
                decoded_metadata.append(string)
                ind += append_index
            elif char == 'i':
                integer, append_index = self.decode_integer(bencoded_data[ind:])
                decoded_metadata.append(integer)
                ind += append_index
            else:
                raise Exception('file: Некорректный символ')

        return decoded_metadata

    def decode_string(self, bencoded_data: bytes) -> tuple[str, int]:
        length = ''
        ind = 0

        for byte in bencoded_data:
            char = chr(byte)
            if char.isdigit():
                length += char
            elif char == ":":
                ind += 1
                break
            else:
                raise Exception('string: Некорректный символ')
            ind += 1
        else:
            raise Exception('string: Нет :')

        length = ind + int(length)

        return bencoded_data[ind:length].decode('utf-8'), length

    def decode_integer(self, bencoded_data: bytes) -> tuple[int, int]:
        integer = ''
        length = 0

        for byte in bencoded_data:
            char = chr(byte)
            if char.isdigit():
                integer += char
            elif char == "i":
                pass
            elif char == "e":
                length += 1
                break
            else:
                raise Exception('integer: Некорректный символ')
            length += 1
        else:
            raise Exception('integer: Нет e')

        return int(integer), length
