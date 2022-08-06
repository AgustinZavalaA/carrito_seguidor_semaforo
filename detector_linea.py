import cv2


def main() -> None:
    # analizar el video
    ancho = 640
    alto = 480

    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, ancho)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, alto)

    while True:
        # leer un frame del video
        _, frame = cap.read()
        # convertir el frame a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # detectar lineas negras en el frame
        lineas = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)[1]
        # dilatar las lineas para quedarnos con las mas largas
        lineas = cv2.dilate(lineas, None, iterations=2)

        lineas_cnts, lineas_hier = cv2.findContours(
            lineas.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        cv2.drawContours(frame, lineas_cnts, -1, (0, 255, 0), 3)

        if len(lineas_cnts) >= 2:
            areaArray = []
            for i, c in enumerate(lineas_cnts):
                area = cv2.contourArea(c)
                areaArray.append(area)

            # first sort the array by area
            sorteddata = sorted(
                zip(areaArray, lineas_cnts), key=lambda x: x[0], reverse=True
            )

            linea_der = sorteddata[0][1]
            linea_izq = sorteddata[1][1]

            centros = []
            for c in [linea_der, linea_izq]:
                # compute the center of the contour
                M = cv2.moments(c)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                centros.append((cX, cY))
                # draw the contour and center of the shape on the image
                cv2.circle(frame, (cX, cY), 7, (0, 0, 255), -1)

            centro_final = (
                (centros[0][0] + centros[1][0]) / 2,
                (centros[0][1] + centros[1][1]) / 2,
            )
            cv2.circle(
                frame, (int(centro_final[0]), int(centro_final[1])), 7, (255, 0, 0), -1
            )

        cv2.imshow("img", frame)
        cv2.imshow("lineas", lineas)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
    pass
