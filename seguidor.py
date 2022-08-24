import cv2
import time
import numpy as np


def main() -> None:
    # analizar el video
    ancho = 640 // 2
    alto = 480 // 2

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, ancho)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, alto)

    try:

        while True:
            # leer un frame del video
            _, frame = cap.read()
            # frame = frame[180:240, :, :]
            # convertir el frame a escala de grises
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # detectar color rojo
            lower = np.array([155, 25, 0])
            upper = np.array([179, 255, 255])
            mask = cv2.inRange(hsv, lower, upper)

            print(f"red size: {cv2.countNonZero(mask)}")
            if cv2.countNonZero(mask) > 10_000:
                continue

            # detectar lineas negras en el frame
            lineas = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)[1]
            # dilatar las lineas para quedarnos con las mas largas
            lineas = cv2.dilate(lineas, None, iterations=2)

            lineas_cnts, lineas_hier = cv2.findContours(
                lineas.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )

            cv2.drawContours(frame, lineas_cnts, -1, (0, 255, 0), 3)

            if lineas_cnts:
                c = max(lineas_cnts, key=cv2.contourArea)

                # compute the center of the contour
                M = cv2.moments(c)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                # draw the contour and center of the shape on the image
                cv2.circle(frame, (cX, cY), 7, (0, 0, 255), -1)

            cv2.imshow("img", frame)
            # cv2.imshow("lineas", lineas)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break
    except KeyboardInterrupt:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
    pass
