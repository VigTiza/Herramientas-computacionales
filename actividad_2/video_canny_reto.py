#------------------------------------------------------------------------------------------------------------------
#   Real-time video capture with Canny edge detection
#------------------------------------------------------------------------------------------------------------------

import cv2

cam_port = 0
cam = cv2.VideoCapture(cam_port)

while True:
    result, frame = cam.read()
    if result:
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Apply Canny edge detection
        edges = cv2.Canny(gray, 100, 200)
        # Show original and edges side by side
        combined = cv2.hconcat([frame, cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)])
        cv2.imshow("Original | Canny Edges (Press q to quit)", combined)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("No image detected")
        break

cam.release()
cv2.destroyAllWindows()

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------
