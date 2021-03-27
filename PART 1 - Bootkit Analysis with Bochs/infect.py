mbr_file = open("infected_mbr.bin", "rb")
mbr = mbr_file.read()
mbr_file.close()

disk_image_file = open("c.img", "r+b")
disk_image_file.seek(0)
disk_image_file.write(mbr)
disk_image_file.close()
