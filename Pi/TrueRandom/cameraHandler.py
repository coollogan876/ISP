from picamera2 import Picamera2, Preview

class cameraHandler:
    def __init__(self, preview=True):
        self.camera = Picamera2()
        self.preview = preview
        self.camera.config(create_preview_configuration())
        if (preview):
            self.camera.start_preview(Preview.QTGL)
        self.camera.start()
