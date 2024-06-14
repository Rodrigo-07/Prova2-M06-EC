# Função de extrair frames
# Importar haars cascaeds
# Função de detectar caras em cada frame ou imagem
# Juntar frames no vídeo

# Estrategia, usar 3 haars cascade para achar melhor as caras

import cv2

frames = []

# Extrair frames do vídeo
def frame_extract(video_path):
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames

def face_detection_haar(frame, face_cascade, body_cascade, eye_cascade):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # person_bodies = body_cascade.detectMultiScale(frame_gray, scaleFactor=1.05, minNeighbors=5, minSize=(30, 30))
    # print(f'Foram encontrados {len(person_bodies)} corpos')

    faces_validated = []

    # for (x, y, w, h) in person_bodies:

    #     faces_validated.append((x, y, w, h))

        # body_frame = frame[y:y+h, x:x+w]

        # faces = face_cascade.detectMultiScale(body_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        # print(f'Foram encontrados {len(faces)} faces')

    faces = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=6, minSize=(30, 30))

    print(f'Foram encontrados {len(faces)} faces')

    for (x, y, w, h) in faces:
        face_frame = frame_gray[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(face_frame, scaleFactor=1.1, minNeighbors=7, minSize=(30, 30))

        print(f'Foram encontrados {len(eyes)} olhos')

        if len(eyes) > 0:
            faces_validated.append((x, y, w, h))

    return faces_validated

video_frames = frame_extract("la_cabra.mp4")

total_frames = len(video_frames)

print(f"Foram extraidos {total_frames} frames")

body_haar_cascade = cv2.CascadeClassifier("cascades/haarcascade_upperbody.xml")
face_haar_ascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
eye_haar_cascade = cv2.CascadeClassifier("cascades/haarcascade_eye.xml")

frames_classified = []

for i in range(total_frames):
    frame_now = video_frames[i]

    faces = face_detection_haar(frame_now, face_haar_ascade, body_haar_cascade, eye_haar_cascade)

    for (x, y, w, h) in faces:
            cv2.rectangle(frame_now, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame_now, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    frames_classified.append(frame_now)

# Exportar o vídeo fainal 

print(len(frames_classified))

fps = 30 
height, width, _ = frames_classified[0].shape
width_resiezed = width // 2
height_resiezed = height // 2

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter("video_final.mp4", fourcc, fps, (width_resiezed, height_resiezed))

for frame in frames_classified:
    resized_frame = cv2.resize(frame, (width_resiezed, height_resiezed))
    video.write(resized_frame)

video.release()
cv2.destroyAllWindows()



