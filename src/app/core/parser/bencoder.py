class Bencoder:
    def decode_file(self, bencoded_data: bytes):
        ind = 0

        while ind < len(bencoded_data):
            char = chr(bencoded_data[ind])
            if char.isdigit():
                value, append_index = self.decode_string(bencoded_data[ind:])
            elif char == 'i':
                value, append_index = self.decode_integer(bencoded_data[ind:])
            else:
                raise Exception('file: Некорректный символ')

            ind += append_index
            yield value

    def decode_string(self, bencoded_data: bytes) -> tuple[str, int]:
        if 58 not in bencoded_data:
            raise Exception('string: Нет :')

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
