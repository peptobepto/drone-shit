import cv2
import random

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

vid = cv2.VideoCapture(0)

# Set the desired width and height
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920 // 2)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080 // 2)

def detect_bounding_box(video_frame):
    gray_image = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        cv2.rectangle(video_frame, (x, y), (x + w, y + h), (r, g, b), 4)

        box_x = x + w // 2
        box_y = y + h // 2
        frame_center_x = video_frame.shape[1] // 2
        frame_center_y = video_frame.shape[0] // 2

        if box_y < frame_center_y:
            position = "top"
        else:
            position = "bottom"

        if box_x < frame_center_x:
            position += " left"
        else:
            position += " right"

        cv2.putText(video_frame, position, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (r, g, b), 2)

    return faces
    #big mac form mcdonalds with the drink is what i want
while True:
    result, video_frame = vid.read()
    if result is False:
        break

    faces = detect_bounding_box(video_frame)

    cv2.imshow("THE FOG!!! THE FOG IS COMING!!!!!!!!", video_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
