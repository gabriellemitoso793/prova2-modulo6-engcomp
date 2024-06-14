import cv2
import os

video_path = "/home/gabriellemitoso/Documents/prova2-modulo6-engcomp/la_cabra.mp4"

# checa se o arquivo existe
if not os.path.exists(video_path):
    print(f"Arquivo de vídeo {video_path} não existe.")
else:
    vidcap = cv2.VideoCapture(video_path)

    if not vidcap.isOpened():
        print("Não foi possível abrir o arquivo de vídeo")
    else:
        success, image = vidcap.read()
        count = 0

        while success:
            success, image = vidcap.read()
            if success:
                print(f'Fazendo um novo frame: {success}')
                cv2.imwrite(f"frame{count}.jpg", image) 
                count += 1

        vidcap.release()
        print(f"Criado {count} frames.")

        # verifica se há frames para processar
        if count > 0:
            face_classifier1 = cv2.CascadeClassifier(
                cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
            )
            face_classifier2 = cv2.CascadeClassifier(
                cv2.data.haarcascades + "haarcascade_eye.xml"
            )

            # altura e tamanho do frame
            frame = cv2.imread("frame0.jpg")
            height, width, layers = frame.shape

            # define o tipo de arquivo de vídeo e cria o objeto de vídeo
            fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
            out = cv2.VideoWriter('output_video.mp4', fourcc, 30.0, (width, height))

            for i in range(count):
                # carrega e salva cada frame
                frame_path = f"frame{i}.jpg"
                image = cv2.imread(frame_path)
                # verifica se o frame foi carregado corretamente
                if image is not None:
                    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    
                    # detecta faces em cada frame
                    faces1 = face_classifier1.detectMultiScale(
                        gray_image, scaleFactor=1.2, minNeighbors=12, minSize=(40, 40)
                    )
                    # detecta olhos em cada frame para garantir que é uma pessoa
                    eyes1 = face_classifier2.detectMultiScale(
                        gray_image, scaleFactor=1.2, minNeighbors=12, minSize=(40, 40)
                    )
                    
                    for (x, y, w, h) in faces1:
                        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 127), 2)
                    
                    for (x, y, w, h) in eyes1:
                        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
                    
                    cv2.imwrite(f"frame_with_faces{i}.jpg", image)
                
                    out.write(image)

            out.release()
            print("Identificação e vídeo feitos")
        else:
            print("Nada foi identificado no vídeo")