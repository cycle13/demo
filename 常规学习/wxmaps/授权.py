import hashlib


def readquan():
    x = open('data/orgin.txt','r')
    y = x.read()
    x.close()
    fmd5 = hashlib.md5(y.encode("utf-8"))
    ls = fmd5.hexdigest()[0:10]+fmd5.hexdigest()[20:30]
    fmd55 = hashlib.md5(ls.encode("utf-8"))
    ll = fmd55.hexdigest()[5:11]+fmd55.hexdigest()[15:28]
    print(ll)


readquan()
