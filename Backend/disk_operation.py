import sys
import os

SECTOR_SIZE = 512
Reserved_region = 0

address_offset = 0

# Loigal_start_address = Reserved_region + (address_offset * sector_size) #translation

# search all the disk in ur environment
drives_path = [r"\\.\PhysicalDrive0",
               r"\\.\PhysicalDrive1",
               r"\\.\PhysicalDrive2",
               r"\\.\PhysicalDrive3"]

# disk = open(drives_path[3],'rb')

boot_sector_pattern = [0xeb, 0x58, 0x90]  #


# readout_data = disk.readline(3)#

def Find_Boot_sector(drive):
    boot_sector_addr = 0;
    disk = open(drive, 'rb')
    while True:
        disk_offset = disk.seek(boot_sector_addr * SECTOR_SIZE)
        readout_data = disk.readline(3)
        if readout_data[0] == boot_sector_pattern[0] and readout_data[1] == boot_sector_pattern[1] and readout_data[
            2] == boot_sector_pattern[2]:
            break;
        else:
            boot_sector_addr += 1

    if boot_sector_addr != 0:
        print("Reserved the ", boot_sector_addr, " sectors ! ")
    else:
        print("No Reserved Region !!!")

    return boot_sector_addr


# ans = Find_Boot_sector(drives_path[3])

class Disk_struct:
    drives_path = [r"\\.\PhysicalDrive0",
                   r"\\.\PhysicalDrive1",
                   r"\\.\PhysicalDrive2",
                   r"\\.\PhysicalDrive3"]
    disk = 0
    logical_offset = 0
    logical_start  = 0
    def __init__(self, drive):
        drives_path[drive]
        print("Constructor", drives_path[drive])
        self.disk = drives_path[drive]
        #self.getBootSector(self.disk)
        self.logical_offset = self.getBootSector(self.disk)
        self.logical_start = self.logical_offset #physical_Address + offset = Logical_start_Address
        print(self.disk)

    def getBootSector(self, disk_path):
        boot_sector_addr = 0;
        disk = open(disk_path, 'rb')
        while True:
            disk_offset = disk.seek(boot_sector_addr * SECTOR_SIZE)
            readout_data = disk.readline(3)
            if readout_data[0] == boot_sector_pattern[0] and readout_data[1] == boot_sector_pattern[1] and readout_data[
                2] == boot_sector_pattern[2]:
                break;
            else:
                boot_sector_addr += 1

        if boot_sector_addr != 0:
            print("Reserved the ", boot_sector_addr, " sectors ! ")
        else:
            print("No Reserved Region !!!")

        return boot_sector_addr


def main():
    d1 = Disk_struct(2)


if __name__ == '__main__':
    main()


