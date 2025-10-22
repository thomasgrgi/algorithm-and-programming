class Device:
	def __init__(self, brand: str, model: str):
		self.brand = brand
		self.model = model
		self.powered_on = False

	def power_on(self):
		self.powered_on = True
		# Only print if device is generic (not subclass), to avoid duplicate messages
		if type(self) is Device:
			print(f"{self.brand} {self.model}: Powering on (generic device)")

	def power_off(self):
		self.powered_on = False
		print(f"{self.brand} {self.model}: Powering off")

	def get_device_info(self):
		return f"{self.brand} {self.model} - powered_on={self.powered_on}"


class PC(Device):
	def __init__(self, brand: str, model: str, cpu: str):
		super().__init__(brand, model)
		self.cpu = cpu

	# override power_on to perform boot sequence
	def power_on(self):
		super().power_on()
		print(f"{self.brand} {self.model}: Booting up PC (CPU: {self.cpu})")

	def get_device_info(self):
		base = super().get_device_info()
		return base + f" | type=PC | cpu={self.cpu}"


class Laptop(Device):
	def __init__(self, brand: str, model: str, battery_level: int = 100):
		super().__init__(brand, model)
		self.battery_level = battery_level

	# override power_on to check battery and enable power-saving
	def power_on(self):
		if self.battery_level < 5:
			print(f"{self.brand} {self.model}: Battery too low ({self.battery_level}%). Please charge before powering on.")
			return
		super().power_on()
		print(f"{self.brand} {self.model}: Booting up laptop (battery at {self.battery_level}%)")

	def get_device_info(self):
		base = super().get_device_info()
		return base + f" | type=Laptop | battery={self.battery_level}%"

	def process_task(self, task: str):
		if not self.powered_on:
			print(f"{self.brand} {self.model}: Cannot process task — device is off")
			return
		if self.battery_level <= 0:
			print(f"{self.brand} {self.model}: Cannot process task — battery is dead")
			return
		print(f"{self.brand} {self.model}: Processing task '{task}'")
		# Simulate battery drain
		self.battery_level -= 5
		if self.battery_level < 0:
			self.battery_level = 0
		print(f"{self.brand} {self.model}: Battery level after task: {self.battery_level}%")


class Smartphone(Device):
	def __init__(self, brand: str, model: str, sim_inserted: bool = True):
		super().__init__(brand, model)
		self.sim_inserted = sim_inserted

	# override power_on to check SIM and network
	def power_on(self):
		super().power_on()
		print("Powering on smartphone...")
		if not self.sim_inserted:
			print(f"{self.brand} {self.model}: No SIM card detected — cellular services disabled")
		else:
			print(f"{self.brand} {self.model}: SIM card installed - connecting to cellular network")

	def send_message(self, number: str, text: str):
		if not self.powered_on:
			print(f"{self.brand} {self.model}: Cannot send message — device is off")
			return
		if not self.sim_inserted:
			print(f"{self.brand} {self.model}: Cannot send message — no SIM")
			return
		print(f"{self.brand} {self.model}: Sending SMS to {number}: {text}")

	def get_device_info(self):
		base = super().get_device_info()
		return base + f" | type=Smartphone | sim_inserted={self.sim_inserted}"


def demo_polymorphism():
	devices = [
		PC("MSI", "MAG B550 TOMAHAWK", cpu="Intel i7"),
		Laptop("ASUS", "Zenbook Duo", battery_level=9),
		Smartphone("Apple", "iPhone 15 Pro Max", sim_inserted=True),
		Smartphone("OnePlus", "Open", sim_inserted=False),
	]

	print("--- Polymorphism demo: power_on for all devices ---")
	for d in devices:
		# same method call, different behaviors depending on class
		d.power_on()
		print(d.get_device_info())
		print()

	print("--- Polymorphism demo: send_message where available ---")
	for d in devices:
		if hasattr(d, "send_message"):
			# call the subclass-specific method
			d.send_message("+1234567890", "I like polymorphism")
			
    # test battery laptop
	devices[1].process_task("Compile code")
	devices[1].power_off()
	devices[1].process_task("Run tests") # should not work, powered off
	devices[1].power_on() # should not work, battery 4% < 5%

	


if __name__ == "__main__":
	demo_polymorphism()

