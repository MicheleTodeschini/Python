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

        # DA BUTTARE QUESTA VARIABILE
        self.counter = 0

        self.setWindowTitle("Camera Recognition")
        self.setGeometry(700, 200, 800, 600)

        # per dire a MediaPipe quale modello usare, quella che cercherà i landmark della mano, quella che gestisce la config del rilevatore e come elaborare le immagini (facendo riferimento a VisionRunningMode, che dopo  viene specificato VIDEO)
        BaseOptions = mp.tasks.BaseOptions
        HandLandmarker = mp.tasks.vision.HandLandmarker
        HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
        VisionRunningMode = mp.tasks.vision.RunningMode

        # percorso del file di mediapipe, file da installare NON da creare a mano
        model_path = os.path.join(os.path.dirname(__file__), "hand_landmarker.task")

        # Configurazione MediaPipe (il video, quante mani deve seguire etc)
        options = HandLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=model_path),
            running_mode=VisionRunningMode.VIDEO,
            num_hands=1,
            min_hand_detection_confidence=0.5,
            min_hand_presence_confidence=0.5,
            min_tracking_confidence=0.5,
        )

        # Crea il detector
        self.detector = HandLandmarker.create_from_options(options)

        # creazione della webcam, 0 valore della webcam di default
        self.cam = cv2.VideoCapture(0)

        if not self.cam.isOpened():
            print(
                "Error: Impossible starting the webcam. Try opening it or enabling it from the settings (f10 for me eheh )"
            )

        # GUI
        self.camera_label = QLabel()

        self.camera_label.setAlignment(Qt.AlignCenter)

        central_widget = QWidget()

        layout = QVBoxLayout()

        layout.addWidget(self.camera_label)

        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

        # Timer che serve a prendere una foto ogni 30ms e a renderla quindi un video

        self.timer = QTimer()

        self.timer.timeout.connect(self.update_frame)

        self.timer.start(30)

    def update_frame(self):

        success, frame = self.cam.read()

        if not success:
            print("Impossibile leggere il fotogramma.")
            return

        # serve a girare la webcam, sennò sarei a testa in giù
        frame = cv2.flip(frame, 1)

        # trasformare l'immagine in un set di colori RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

        timestamp = int(time.time() * 1000)

        result = self.detector.detect_for_video(mp_image, timestamp)

        # creazione dei landmark sulla mano
        if result.hand_landmarks:
            # print(result)

            points = []
            for landmark in result.hand_landmarks[0]:
                points.append((landmark.x, landmark.y, landmark.z))

            wrist = points[0]
            thumb_base = points[1]
            thumb_tip = points[4]
            index_base = points[5]
            index_tip = points[8]
            middle_base = points[9]
            middle_tip = points[12]
            ring_base = points[13]
            ring_tip = points[16]
            pinky_base = points[17]
            pinky_tip = points[20]
            # print(index_tip)

            if (
                index_tip[1] < middle_tip[1]
                and ring_tip[1] < middle_tip[1]
                and pinky_tip[1] < middle_tip[1]
            ):
                self.counter += 1
                print("three_up", self.counter)
                gesture = "three_up"
                self.changed_gesture.emit(gesture)
            elif thumb_tip[1] > wrist[1]:
                self.counter += 1
                print("thumb_down", self.counter)
                gesture = "thumb_down"
                self.changed_gesture.emit(gesture)
            elif (
                thumb_tip[1] < ring_tip[1]
                and index_tip[1] < ring_tip[1]
                and middle_tip[1] < ring_tip[1]
                and thumb_tip[1] < pinky_tip[1]
                and index_tip[1] < pinky_tip[1]
                and middle_tip[1] < pinky_tip[1]
            ):
                self.counter += 1
                print("pistol", self.counter)
                gesture = "pistol"
                self.changed_gesture.emit(gesture)
            elif all(
                tip[1] < finger[1]
                for tip in [thumb_tip, index_tip, pinky_tip]
                for finger in [middle_tip, ring_tip]
            ):
                gesture = "spiderman"
                self.changed_gesture.emit(gesture)

            for hand_landmarks in result.hand_landmarks:

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

        height, width, channel = frame.shape

        bytes_per_line = channel * width

        q_image = QImage(
            frame.data, width, height, bytes_per_line, QImage.Format_RGB888
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

        if self.gesture == "three_up":
            three_up = cv2.imread(
                r"C:\Users\ASUS\Desktop\progetti vsc\Python\HelloWorld\55. webcam_recognition_hand\photo\three_up.jpg"
            )
            height, width, channel = three_up.shape
            bytes_per_line = channel * width
            q_three_up = QImage(
                three_up.data, width, height, bytes_per_line, QImage.Format_BGR888
            )
            pixmap = QPixmap.fromImage(q_three_up)
            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio)
            )
        elif self.gesture == "thumb_down":
            thumb_down = cv2.imread(
                r"C:\Users\ASUS\Desktop\progetti vsc\Python\HelloWorld\55. webcam_recognition_hand\photo\thumb_down.png"
            )
            height, width, channel = thumb_down.shape
            bytes_per_line = channel * width
            q_thumb_down = QImage(
                thumb_down.data, width, height, bytes_per_line, QImage.Format_BGR888
            )
            pixmap = QPixmap.fromImage(q_thumb_down)
            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio)
            )
        elif self.gesture == "pistol":
            pistol = cv2.imread(
                r"C:\Users\ASUS\Desktop\progetti vsc\Python\HelloWorld\55. webcam_recognition_hand\photo\pistol.jpg"
            )
            height, width, channel = pistol.shape
            bytes_per_line = channel * width
            q_pistol = QImage(
                pistol.data, width, height, bytes_per_line, QImage.Format_BGR888
            )
            pixmap = QPixmap.fromImage(q_pistol)
            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio)
            )
        elif self.gesture == "spiderman":
            spiderman = cv2.imread(
                r"C:\Users\ASUS\Desktop\progetti vsc\Python\HelloWorld\55. webcam_recognition_hand\photo\spiderman.jpg"
            )
            height, width, channel = spiderman.shape
            bytes_per_line = channel * width
            q_spiderman = QImage(
                spiderman.data, width, height, bytes_per_line, QImage.Format_BGR888
            )
            pixmap = QPixmap.fromImage(q_spiderman)
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
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
