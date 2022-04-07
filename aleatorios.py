import nacl.utils as pynacl

if __name__ == "__main__":
    bs = pynacl.random(size=128)
    for c in bs:
        print('{0:X}'.format(c), end=" ")
