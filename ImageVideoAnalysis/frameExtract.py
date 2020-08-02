import cv2

# Function to extract frames
def FrameCapture(path):
    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        cv2.imwrite("frame%d.jpg" % count, image)

        count += 1


# Driver Code
if __name__ == '__main__':
    # Calling the function
    FrameCapture("C:\\Users\\divya\\Documents\\data science\\internship celebal\\screen_recorder_video_2019_07_6_18_14_41\\b.mp4")