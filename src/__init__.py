"""Python Practice Project - приложение для работы с изображением"""

__version__ = "1.0.0"

from .interface import Interface
from .draw_line import DrawGreenLine
from .camera_capture import CameraCapture

__all__ = [
    "Interface",
    "DrawGreenLine",
    "CameraCapture"
]