import cv2
import pytesseract
import numpy as np


def binarizacion(img):
    imagen_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imagen_gris = cv2.GaussianBlur(imagen_gris, (5, 5), 0)
    _, imagen_binaria = cv2.threshold(imagen_gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return imagen_binaria


def conv_texto(imagen_binaria):
    texto = pytesseract.image_to_string(imagen_binaria, lang='spa', config='--psm 6')
    return texto


video = cv2.VideoCapture(0)
texto_detectado = ""  # Se mantiene entre capturas

while True:
    check, frame = video.read()
    if not check:
        break

    # Coordenadas del ROI
    x1, y1, x2, y2 = 300, 100, 600, 300
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    # Extraer y procesar ROI
    ROI = frame[y1+5:y2-5, x1+5:x2-5]
    ROI_bin = binarizacion(ROI)

    # Mostrar texto debajo del ROI
    if texto_detectado:
        y_texto = y2 + 30
        cv2.putText(frame, texto_detectado.strip(), (x1, y_texto),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2, cv2.LINE_AA)

    # Mostrar ventanas
    cv2.imshow("Video", frame)
    #cv2.imshow("ROI", ROI)
    cv2.imshow("ROI Binaria", ROI_bin)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        break
    if key == ord('f'):
        print("Captura realizada. Ejecutando OCR...")
        nuevo_texto = conv_texto(ROI_bin)
        if nuevo_texto.strip():
            texto_detectado = nuevo_texto
            print("Texto detectado:")
            print(texto_detectado)
        else:
            print("No se detectó texto. Manteniendo el texto anterior.")

video.release()
cv2.destroyAllWindows()



