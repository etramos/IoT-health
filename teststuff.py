
import usb.core
import usb.util


VID=0x10c4
PID=0x0002

dev=usb.core.find(idVendor=VID, idProduct=PID)
if not dev:
	print "couldn't find"
	exit(1)
print "yes! Found Device, it's the lascar probe"

#dev.ctrl_transfer( reqType, bReq,wVal,wIndex,data)
print dev.bLength ,"size of descriptor"
print dev.bNumConfigurations , "# of possible configurations"
print dev.bDeviceClass , "USB-IF class code"
print dev.bDeviceProtocol , "USB-IF protocol code for device"
print dev.bcdDevice ,  "device release number# in binary coded decimal"
print dev.iManufacturer ,  "index of string descriptor describing manufacturer"
print dev.iProduct ,  "index of string descriptor describing product"

#RANDOM STUFF BELOW PLZ IGNORE
#msg='test'
#assert dev.ctrl_transfer(0x40, CTRL_LOOPBACK_WRITE,0,0,msg)== len(msg)
#ret=dev.ctrl_transfer(0xC0,CTRL_LOOPBACK_READ,0,0,len(msg))
#sret=''.join([chr(x) for x in ret])
#assert sret==msg

print usb.control
exit(0)

