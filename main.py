import cv2
import speech_recognition as sr

def take_picture(cap):
    # Capture an image from the webcam
    ret, frame = cap.read()

    # Save the captured frame as an image file (you can use a timestamped filename)
    filename = "captured_image.jpg"
    cv2.imwrite(filename, frame)

    print(f"Picture taken and saved as {filename}")

def main():
    recognizer = sr.Recognizer()

    cap = None  # Initialize the cap variable outside the loop
    webcam_opened = False

    with sr.Microphone() as source:
        print("Say 'open camera' to open the webcam and 'shutter' to take a picture!")
        recognizer.adjust_for_ambient_noise(source)

        while True:
            audio = recognizer.listen(source)

            try:
                command = recognizer.recognize_google(audio).lower()

                if "open camera" in command and not webcam_opened:
                    # Open the webcam
                    cap = cv2.VideoCapture(0)
                    _, frame = cap.read()
                    cv2.imshow('Webcam', frame)
                    cv2.waitKey(1)
                    webcam_opened = True

                    print("Webcam opened successfully.")

                elif "shutter" in command and webcam_opened:
                    # Take a picture if the webcam is open
                    take_picture(cap)
                    print("Image captured!")

                elif "close camera" in command and webcam_opened:
                    # Close the webcam if it's open
                    cap.release()
                    cv2.destroyAllWindows()
                    webcam_opened = False
                    print("Webcam closed.")



            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()