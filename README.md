# 🧠 OCR en tiempo real con OpenCV y Tesseract | Real-time OCR with OpenCV and Tesseract

🎥 Proyecto de visión por computadora que captura texto en vivo desde la cámara web usando OpenCV y Tesseract OCR en español.  
🎯 Real-time OCR app using OpenCV and Tesseract (Spanish language support).

---

## ⚙️ Tecnologías usadas | Technologies used

- Python 3.12.3
- OpenCV-Python 4.11.0.86
- Pytesseract 0.3.13
- Tesseract-OCR (idioma: español)  
- Sistema operativo: Linux Ubuntu

---

## 🎬 Funcionamiento | How it works

1. Se abre la cámara y se dibuja un rectángulo (ROI).
2. Al presionar `f`, se captura la región y se procesa para extraer texto.
3. El texto detectado se muestra en pantalla debajo del ROI.(Región de Interés)
4. Presioná `s` para salir del programa.

> 🔤 The detected text is shown in real-time below the ROI.

---

## ⌨️ Controles | Controls

| Tecla | Acción                  | Key | Action                  |
|-------|--------------------------|-----|---------------------------|
| `f`   | Capturar texto (OCR)     | `f` | Capture text (OCR)       |
| `s`   | Salir del programa       | `s` | Exit the program         |

---

## 📸 Demo VIDEO

> 🎥 Video incluido en el repositorio para ver el funcionamiento real.

---

## 🧪 Mejora posible | Possible improvement

- Guardar texto en `.txt`
- Cambiar idioma dinámicamente
- Interfaz con botones (GUI)
