import sys, os
from Crypto.Cipher import AES


def encrypt(key,iv,msg):
    try:
        enc_suite = AES.new(key, AES.MODE_CBC, iv)
    except ValueError:
        print "Invalid IV/Key Sizes!"
        exit(0)
    return enc_suite.encrypt(msg)


def decrypt(key,iv,msg):
    try:
        dec_suite = AES.new(key, AES.MODE_CBC, iv)
    except ValueError:
        print "Invalid IV/Key Sizes!"
        exit(0)
    return dec_suite.decrypt(msg)


def usage():
    print "Incorrect Usage!"
    print "python AES_CBC.py -<mode> <key> <iv> <TEXT>"


def padding_handler(text):
    '''
    This can only be used on messages. Keys and
    IVs simply have to be properly configured for
    any kind of security at all.
    :param text:
    :return:
    '''
    textout = text
    nchars = len(list(text))
    if nchars%16==0:
        return text
    else:
        npad = (256-len(text))
        for i in range(npad):
            textout += 'x'
        if len(textout) % 16 == 0:
            return str(textout)


def main():
    if len(sys.argv) < 5:
        usage()
    else:
        key = sys.argv[2]
        iv = sys.argv[3]
        msg = padding_handler(sys.argv[4])
        if sys.argv[1] == '-d':
            print "\t\t:: Decrypting ::"
            ans = decrypt(key,iv,msg)
            print ans
        if sys.argv[1] == '-e':
            # print "\t\t:: Encrypting :: "
            ciph_txt = encrypt(key,iv,msg)
            print ciph_txt


if __name__ == '__main__':
    main()
