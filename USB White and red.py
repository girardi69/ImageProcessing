import cv2
import numpy as np

def start_camera_stream(camera_index=1):  # Default to index 1 for USB camera
    # Initialize the USB camera (typically index 1, but can be changed)
    cap = cv2.VideoCapture(camera_index)
    
    # Check if the camera opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open camera at index {camera_index}.")
        return
    
    print(f"Camera at index {camera_index} accessed successfully. Press 'q' to quit.")
    
    # Capture and display frames in a loop
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # If frame is read correctly, ret is True
        if not ret:
            print("Error: Can't receive frame. Exiting...")
            break
        
        # Extract only the red channel
        # OpenCV uses BGR format, so red is the third channel (index 2)
        red_channel = np.zeros_like(frame)
        red_channel[:, :, 2] = frame[:, :, 2]  # Copy only the red channel
        
        # Display both the original frame and the red channel
        cv2.imshow('Original Camera Feed', frame)
        cv2.imshow('Red Channel Only', red_channel)
        
        # Handle key presses - increase wait time to 30ms for better key detection
        key = cv2.waitKey(30) & 0xFF  # Add bitmask to handle key codes consistently across platforms
        
        # Save image when 's' is pressed
        if key == ord('s'):
            cv2.imwrite('captured_image.jpg', frame)
            cv2.imwrite('red_channel_image.jpg', red_channel)
            print("Images saved as 'captured_image.jpg' and 'red_channel_image.jpg'")
        
        # Break the loop when 'q' is pressed
        if key == ord('q'):
            print("Q key pressed. Exiting...")
            break
        
        # Alternative exit with ESC key
        if key == 27:  # ESC key
            print("ESC key pressed. Exiting...")
            break
    
    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()
    
    # Additional attempt to close windows properly
    for i in range(1, 5):
        cv2.waitKey(1)

# Start the camera stream with USB camera (typically index 1)
# You can change this number if your USB camera uses a different index
if __name__ == "__main__":
    start_camera_stream(1)
