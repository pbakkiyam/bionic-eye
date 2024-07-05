# Function to display the bionic eye simulation
def bionic_eye_simulation():
    # Open a connection to the webcam
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            print("Error: Could not read frame.")
            break

        # Detect edges in the frame
        edges = detect_edges(frame)

        # Dilate the edges to expand them
        dilated_edges = cv2.dilate(edges, None, iterations=2)

        # Create a black image (dark) with the same dimensions as the frame
        dark_image = np.zeros_like(frame)

        # Set the pixels corresponding to edges in the dark image to white (light)
        dark_image[dilated_edges != 0] = [255, 255, 255]

        # Display the original frame and the processed frame
        cv2.imshow('Original Frame', frame)
        cv2.imshow('Bionic Eye Simulation', dark_image)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

# Run the bionic eye simulation
bionic_eye_simulation()
