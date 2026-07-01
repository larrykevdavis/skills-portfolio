import cv2

videoCaptureObject = cv2.VideoCapture(0)

upper_left = (0, 0)
bottom_right = (200, 310)

result = True
while(result):
    ret,image_frame = videoCaptureObject.read()
    image_frame = cv2.flip(image_frame , 1)
    #Rectangle marker
    r = cv2.rectangle(image_frame, upper_left, bottom_right, (50, 50, 200), 5)
    rect_img = image_frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]
    
    image_grayscale = cv2.cvtColor(rect_img, cv2.COLOR_BGR2GRAY)
    image_grayscale_blurred = cv2.GaussianBlur(image_grayscale, (7,7), 0)
    image_canny = cv2.Canny(image_grayscale_blurred, 10, 80)
    _, mask = image_canny_inverted = cv2.threshold(image_canny, 30, 255, cv2.THRESH_BINARY_INV)
    
    #Conversion for 3 channels to put back on original image (streaming)
    sketcher_rect_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    
    #Replacing the sketched image on Region of Interest
    image_frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]] = sketcher_rect_rgb

    cv2.imshow("test", image_frame)
    k = cv2.waitKey(1)

    if k%256 == 27:
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        cv2.imwrite("input_image.jpg",image_frame)
        img = cv2.imread("input_image.jpg")

videoCaptureObject.release()
cv2.destroyAllWindows()