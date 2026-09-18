import sys
import time
import os

import cv2
import mediapipe as mp

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap


class MainWindow(QMainWindow):
    changed_gesture = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Camera Recognition")
        self.setGeometry(700, 200, 800, 600)

        # MediaPipe Gesture Recognizer
        BaseOptions = mp.tasks.BaseOptions
        GestureRecognizer = mp.tasks.vision.GestureRecognizer
        GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
        VisionRunningMode = mp.tasks.vision.RunningMode

        # Percorso del modello di MediaPipe
        model_path = os.path.join(os.path.dirname(__file__), "gesture_recognizer.task")

        # Configurazione MediaPipe
        options = GestureRecognizerOptions(
            base_options=BaseOptions(model_asset_path=model_path),
            running_mode=VisionRunningMode.VIDEO,
            num_hands=1,
            min_hand_detection_confidence=0.5,
            min_hand_presence_confidence=0.5,
            min_tracking_confidence=0.5,
        )

        self.detector = GestureRecognizer.create_from_options(options)

        self.cam = cv2.VideoCapture(0)

        if not self.cam.isOpened():
            print(
                "Error: Impossible starting the webcam. "
                "Try opening it or enabling it from the settings "
                "(f10 for me eheh )"
            )

        # GUI
        self.camera_label = QLabel()
        self.camera_label.setAlignment(Qt.AlignCenter)

        central_widget = QWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.camera_label)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Timer: prende un fotogramma ogni 30 ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):

        success, frame = self.cam.read()

        if not success:
            print("Impossibile leggere il fotogramma.")
            return

        frame = cv2.flip(frame, 1)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Creazione immagine MediaPipe
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

        # Timestamp
        timestamp = int(time.time() * 1000)

        # Riconoscimento
        result = self.detector.recognize_for_video(mp_image, timestamp)

        # I landmark continuano ad essere disponibili
        if result.hand_landmarks:
            gesture = result.gestures[0][0].category_name
            self.changed_gesture.emit(gesture)

            for hand_landmarks in result.hand_landmarks:

                # Disegna i 21 landmark
                for landmark in hand_landmarks:

                    x = int(landmark.x * frame.shape[1])

                    y = int(landmark.y * frame.shape[0])

                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

                # Disegna le connessioni
                connections = [
                    (0, 1),
                    (1, 2),
                    (2, 3),
                    (3, 4),
                    (0, 5),
                    (5, 6),
                    (6, 7),
                    (7, 8),
                    (5, 9),
                    (9, 10),
                    (10, 11),
                    (11, 12),
                    (9, 13),
                    (13, 14),
                    (14, 15),
                    (15, 16),
                    (13, 17),
                    (17, 18),
                    (18, 19),
                    (19, 20),
                    (0, 17),
                ]

                for start, end in connections:

                    x1 = int(hand_landmarks[start].x * frame.shape[1])

                    y1 = int(hand_landmarks[start].y * frame.shape[0])

                    x2 = int(hand_landmarks[end].x * frame.shape[1])

                    y2 = int(hand_landmarks[end].y * frame.shape[0])

                    cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Conversione per Qt
        height, width, channel = frame.shape
        bytes_per_line = channel * width

        q_image = QImage(
            frame.data, width, height, bytes_per_line, QImage.Format_BGR888
        )

        pixmap = QPixmap.fromImage(q_image)

        self.camera_label.setPixmap(
            pixmap.scaled(self.camera_label.size(), Qt.KeepAspectRatio)
        )

    def closeEvent(self, event):

        self.timer.stop()
        self.cam.release()
        self.detector.close()

        event.accept()


class ImageWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image")
        self.setGeometry(700, 200, 800, 600)
        self.image_label = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

        self.gesture = None

        self.timer = QTimer()
        self.timer.timeout.connect(self.show_image)
        self.timer.start(30)

    def update_gesture(self, gesture):
        self.gesture = gesture

    def show_image(self):

        if self.gesture == "Victory":
            victory = cv2.imread(
                r"C:\Users\ASUS\Desktop\progetti vsc\Python\HelloWorld\56. webcam_recognition_gesture\photo\victory.jpg"
            )
            height, width, channel = victory.shape
            bytes_per_line = channel * width
            q_victory = QImage(
                victory.data, width, height, bytes_per_line, QImage.Format_BGR888
            )
            pixmap = QPixmap.fromImage(q_victory)
            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio)
            )
        elif self.gesture == "Pointing_Up":
            pointing_up = cv2.imread(
                r"C:\Users\ASUS\Desktop\progetti vsc\Python\HelloWorld\56. webcam_recognition_gesture\photo\pointing.png"
            )
            height, width, channel = pointing_up.shape
            bytes_per_line = channel * width
            q_pointing_up = QImage(
                pointing_up.data, width, height, bytes_per_line, QImage.Format_BGR888
            )
            pixmap = QPixmap.fromImage(q_pointing_up)
            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio)
            )
        elif self.gesture == "Thumb_Up":
            thumb_up = cv2.imread(
                r"C:\Users\ASUS\Desktop\progetti vsc\Python\HelloWorld\56. webcam_recognition_gesture\photo\thumb_up.jpg"
            )
            height, width, channel = thumb_up.shape
            bytes_per_line = channel * width
            thumb_up = QImage(
                thumb_up.data, width, height, bytes_per_line, QImage.Format_BGR888
            )
            pixmap = QPixmap.fromImage(thumb_up)
            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio)
            )
        elif self.gesture == "Open_Palm":
            open_palm = cv2.imread(
                r"C:\Users\ASUS\Desktop\progetti vsc\Python\HelloWorld\56. webcam_recognition_gesture\photo\open_palm.jpg"
            )
            height, width, channel = open_palm.shape
            bytes_per_line = channel * width
            q_open_palm = QImage(
                open_palm.data, width, height, bytes_per_line, QImage.Format_BGR888
            )
            pixmap = QPixmap.fromImage(q_open_palm)
            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio)
            )
        elif self.gesture == "Closed_Fist":
            closed_fist = cv2.imread(
                r"C:\Users\ASUS\Desktop\progetti vsc\Python\HelloWorld\56. webcam_recognition_gesture\photo\closed_fist.jpg"
            )
            height, width, channel = closed_fist.shape
            bytes_per_line = channel * width
            q_closed_fist = QImage(
                closed_fist.data, width, height, bytes_per_line, QImage.Format_BGR888
            )
            pixmap = QPixmap.fromImage(q_closed_fist)
            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio)
            )


def main():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    image = ImageWindow()
    image.show()

    window.changed_gesture.connect(image.update_gesture)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
