def read_file(file, mode):
    f = open(file, mode)
    b = f.read()
    f.close()
    return b

def write_file(file, mode, bytes):
    f = open(file, mode)
    f.write(bytes)
    f.close()
