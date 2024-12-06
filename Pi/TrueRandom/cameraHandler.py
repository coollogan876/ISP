from picamera2 import Picamera2, Preview

class cameraHandler:
    def __init__(self, preview=True):
        Picamera2.set_logging(Picamera2.ERROR)
        self.camera = Picamera2()
        self.preview = preview
        self.camera.configure(self.camera.create_preview_configuration())
        self.camera.set_controls({"AwbEnable": True, "Contrast": 0.4, "Saturation" : 0.75, "ExposureTime": 5000})
        if (preview):
            self.camera.start_preview(Preview.QTGL)
        self.camera.start()
