import obtain
from initialize import loc
from initialize import create
import data_request

if __name__ == '__main__':
    request_check = input("Get data from LCO or unpack downloaded data? (dl/unpack): ")
    if request_check == 'dl':
        data_request.request()
        unpack_check = input("/nUnpack downloaded data? (y/n): ")
        if unpack_check == 'y':
            obtain.move(loc+'/sdi/temp')
            obtain.process()
            check = input("Move data into target directory? (y/n): ")
            if check == "y":
                tar = input("Enter target: ")
                obtain.movetar(tar)
                obtain.rename(tar)
            elif check != "y" and check != "n":
                print("Error: unknown Input")
    elif request_check == 'unpack':
        download_location = input("Enter LCO data location (leave blank for default=%s/Downloads): " % (loc))
        if download_location == "":
            download_location = "%s/Downloads" % (loc)
        obtain.move(download_location)
        obtain.process()
        check = input("Move data into target directory? (y/n): ")
        if check == "y":
            tar = input("Enter target: ")
            obtain.movetar(tar)
            obtain.rename(tar)
        elif check != "y" and check != "n":
            print("Error: unknown Input")