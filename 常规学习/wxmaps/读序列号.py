import wmi


c = wmi.WMI()
for physical_disk in c.Win32_DiskDrive():
    file_handle = open('1.txt', mode='w')
    file_handle.write(physical_disk.SerialNumber)