# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

"""
def shift_n_letters(letter, n):
    if 97 <= int(ord(letter) + n) < 122:
        return chr(ord(letter) + n)
    elif int(ord(letter) + n) <= 97:
        return chr(122-(96-(int(ord(letter) + n))))
    else:
        return chr((int(ord(letter) + n) - 122) + 96)

"""
def rotate(name , n):
    name2 = list(name)
    name3 = []
    for letter in name2:

        if 97 <= int(ord(letter) + n) < 122:
            name3.append(chr(ord(letter) + n))
        elif int(ord(letter) + n) <= 97:
            name3.append (chr(122 - (96 - (int(ord(letter) + n)))))
        else:
            name3.append(chr((int(ord(letter) + n) - 122) + 96))

        name4 = ''.join(name3)
    return name4


print (rotate ('sarah', 13))
#>>> 'fnenu'
print (rotate('fnenu',13))
#>>> 'sarah'
print (rotate('dave',5))
#>>>'ifaj'
print (rotate('ifaj',-5))
#>>>'dave'
print (rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17))
#>>> ???

print (ord('A'))
print (ord(' '))
print (ord(')'))
print (chr(32))