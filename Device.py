class Device:
	def __init__(self,uid,sid,device_type):
		self.uid = uid
		self.devices = {device_type: sid}

	def add_device(sid,did):
		self.devices[device_type]= sid;

	def remove_device(device_type):
		del devices[device_type];