def read_file(file):
    f = open(file, 'rb')
    b = f.read()
    f.close()
    return b

def write_file(file, bytes):
    f = open(file, 'wb')
    f.write(bytes)
    f.close()
