import storage
import usb_cdc

storage.disable_usb_drive()  # Optional for better reliability
usb_cdc.enable(console=True, data=True)