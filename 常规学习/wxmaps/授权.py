import hashlib
import wmi


def readquan(xulie):
    fmd5 = hashlib.md5(xulie.encode("utf-8"))
    ls = fmd5.hexdigest()[0:10]+fmd5.hexdigest()[20:30]
    fmd55 = hashlib.md5(ls.encode("utf-8"))
    ll = fmd55.hexdigest()[5:11]+fmd55.hexdigest()[15:28]
    print(ll)



# def xulie():
#     c = wmi.WMI()
#     # # 硬盘序列号
#     for physical_disk in c.Win32_DiskDrive():
#         return (physical_disk.SerialNumber)

xulie = 'E823_8FA6_BF53_0001_001B_444A_464A_8C98.'
readquan(xulie)
