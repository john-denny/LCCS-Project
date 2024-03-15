import cv2
import numpy as np

def detect_basketball_hoop(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise and help circle detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Use Hough Circle Transform to detect circles (hoop rim)
    circles = cv2.HoughCircles(
        gray, 
        cv2.HOUGH_GRADIENT, dp=1, minDist=200, param1=50, param2=30, minRadius=120, maxRadius=140)
    
    # If circles are found, draw them
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw the outer circle
            cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)
    
    # Display the result
    cv2.imshow("Basketball Hoop Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_basketball_hoop("hoop.jpg")