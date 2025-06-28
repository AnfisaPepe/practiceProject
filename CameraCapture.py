import cv2
from PIL import Image


class CameraCapture:
    def __init__(self, root):
        self.root = root
        self.camera = None
        self.is_capturing = False

    def open_camera(self):
        self.camera = cv2.VideoCapture(0)
        if not self.camera.isOpened():
            raise Exception("Не удалось открыть камеру")

    def capture(self):
        if self.camera:
            # Здесь фрейм bgr
            status, frame = self.camera.read()
            if status:
                frame_rgd = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Создаем объект PIL
                return Image.fromarray(frame_rgd)
        return None

    def stop_camera(self):
        # Очищаем камеру
        if self.camera:
            self.camera.release()