class Camera:
    def take_photo(self):
        print("Taking a photo...")

class Phone:
    def make_call(self):
        print("Making a call...")

class Smartphone(Camera, Phone):
    def __init__(self):
        super().__init__()  # Calls __init__ from Camera, then Phone
        print("Smartphone is ready!")

    def take_photo(self):
        super().take_photo()  # Calls take_photo from Camera
        print("Smartphone can now take a photo!")

    def make_call(self):
        super().make_call()  # Calls make_call from Phone
        print("Smartphone can now make a call!")

# Create an instance of Smartphone
phone = Smartphone()

# Use the methods from both parent classes
phone.take_photo()
phone.make_call()
