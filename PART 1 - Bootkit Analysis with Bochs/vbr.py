vbr_file = open("partition0.data", "rb")
vbr = vbr_file.read()
vbr_file.close()

disk_image_file = open("c.img", "r+b")
disk_image_file.seek(0x10 * 0x200)
disk_image_file.write(vbr)
disk_image_file.close()