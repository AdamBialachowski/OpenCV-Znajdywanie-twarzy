import cv2

#Pobiera obiekt z kamery 0
capture = cv2.VideoCapture(0)
#otwiera okienko
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#tworzy nowy obiekt CascadeClassifier a w argumęcie jest odnajdywanie głowy
faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

while True:
    #Metoda zwraca coś i obrazek
    _, frame = capture.read()
    #Metoda zmienia obraz zapisany w frame na czarnobiały
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayscale,
        scaleFactor=1.2,  #na jakich danych parametr się uczył ogulnie chodzi o odległość
        minNeighbors=5
        )
    #tworzy prostokont na twarzy
    for x, y, face_width, face_height in faces:
        cv2.rectangle(frame, (x, y), (x+ face_width, y + face_height), (255, 0, 0), 5)


    #wyświetla okno
    cv2.imshow('frame', frame)
    cv2.imshow('gray', grayscale)

    #co 50 milisekund sprawdza czy jest wciśniety klawisz i zapisuje go do zmiennej
    key = cv2.waitKey(50)
    #jeżeli jest to escape=27 to wychodzi z pętli
    if key ==27:
        break
#zwalnia capture
capture.release()