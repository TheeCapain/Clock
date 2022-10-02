import hashlib
from tokenize import String
from passlib.hash import sha512_crypt
desiredhash = "$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0"

def decrypt(nr1, nr2, nr3):
    pw = str(nr1)+str(nr2)+str(nr3)
   
    hashedPW =sha512_crypt.using(salt="penguins", rounds=5000).hash(str(pw))
    if hashedPW == desiredhash:
        print()
        print("PW IS: " + pw)
        print(desiredhash)
        print(hashedPW)
        print("-------------------------------------")
        print("This is the hash we were looking for!")
        print("-------------------------------------")
        print()


def numberBreaker():
    num_list = [1,2,3,4,5,6,7,8,9,0]

    for i in range(0, 9):
        for j in range(0, 9):
          for k in range(0, 9):
                decrypt(num_list[i], num_list[j], num_list[k])    


numberBreaker()
##password = hashlib.sha3_512()
##password.update(b'123')
##print(password.digest())