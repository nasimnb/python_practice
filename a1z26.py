

def encode(plain):
      return [ord(elm) for elm in plain]


def decode(encode):
      return "".join(( chr(elm) for elm in encode))

print(decode([110, 97, 115, 105, 109]))