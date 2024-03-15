import cv2
import numpy as np

def track_orange_blob(min_blob_size=1000):  # Adjust the minimum blob size as needed
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define the range of orange color in HSV
        lower_orange = np.array([0, 100, 100])
        upper_orange = np.array([20, 255, 255])

        # Threshold the image to get only orange colors
        mask = cv2.inRange(hsv, lower_orange, upper_orange)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Find the largest contour
            max_contour = max(contours, key=cv2.contourArea)

            # Calculate the area of the blob
            area = cv2.contourArea(max_contour)

            # Only track if the blob is larger than the threshold
            if area > min_blob_size:
                # Calculate the centroid of the blob
                M = cv2.moments(max_contour)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                # Draw a circle at the centroid
                cv2.circle(frame, (cx, cy), 10, (0, 255, 0), -1)

        # Display the resulting frame
        cv2.imshow('Frame', frame)
        cv2.imshow('Mask', mask)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    track_orange_blob()
