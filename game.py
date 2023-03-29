import cv2
import numpy as np


# Load the original image
img = cv2.imread('Image/image.png')
img1 = img.copy()
img2 = img.copy()
img3 = img.copy()

# Get the current size of the image
height, width = img.shape[:2]

# Set the new size (50% smaller than the original size)
new_height = int(height * 2 / 3)
new_width = int(width * 2 / 3)

# Make a copy of the original image and resize it
img_copy1 = img.copy()
cv2.circle(img_copy1, (400, 400), 20, (0, 0, 255), -1)
cv2.circle(img_copy1, (300, 300), 50, (0, 0, 255), -1)


# Make the changes to the copied image that you want to highlight as the differences

img_copy2 = img.copy()
cv2.circle(img_copy2, (400, 400), 20, (0, 0, 255), -1)
cv2.circle(img_copy2, (300, 300), 50, (0, 0, 255), -1)
cv2.circle(img_copy2, (600, 500), 20, (0, 0, 255), -1)
cv2.circle(img_copy2, (100, 100), 50, (0, 0, 255), -1)


img_copy3 = img.copy()
cv2.circle(img_copy3, (400, 400), 20, (0, 0, 255), -1)
cv2.circle(img_copy3, (300, 300), 50, (0, 0, 255), -1)
cv2.circle(img_copy3, (100, 100), 50, (0, 0, 255), -1)
# cv2.imshow("image1", img_copy3)


diff1 = cv2.absdiff(img1, img_copy1)
# Chuyển đổi sang ảnh xám để dễ xử lý
gray1 = cv2.cvtColor(diff1, cv2.COLOR_BGR2GRAY)

# Áp dụng phép lọc Gaussian để loại bỏ nhiễu
gray1 = cv2.GaussianBlur(gray1, (5, 5), 0)
# Áp dụng ngưỡng để tách ra vùng khác biệt
ret1, thresh1 = cv2.threshold(gray1, 20, 255, cv2.THRESH_BINARY)
# Tìm và vẽ khoanh vùng khác biệt lên ảnh gốc
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.rectangle(img_copy1, (x, y), (x+w, y+h), (0, 0, 255), 2)



diff2 = cv2.absdiff(img2, img_copy2)
# Chuyển đổi sang ảnh xám để dễ xử lý
gray2 = cv2.cvtColor(diff2, cv2.COLOR_BGR2GRAY)

# Áp dụng phép lọc Gaussian để loại bỏ nhiễu
gray2 = cv2.GaussianBlur(gray2, (5, 5), 0)
# Áp dụng ngưỡng để tách ra vùng khác biệt
ret1, thresh1 = cv2.threshold(gray2, 20, 255, cv2.THRESH_BINARY)
# Tìm và vẽ khoanh vùng khác biệt lên ảnh gốc
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.rectangle(img_copy2, (x, y), (x+w, y+h), (0, 0, 255), 2)




diff3 = cv2.absdiff(img3, img_copy3)
# Chuyển đổi sang ảnh xám để dễ xử lý
gray3 = cv2.cvtColor(diff3, cv2.COLOR_BGR2GRAY)

# Áp dụng phép lọc Gaussian để loại bỏ nhiễu
gray3 = cv2.GaussianBlur(gray3, (5, 5), 0)
# Áp dụng ngưỡng để tách ra vùng khác biệt
ret3, thresh3 = cv2.threshold(gray3, 20, 255, cv2.THRESH_BINARY)
# Tìm và vẽ khoanh vùng khác biệt lên ảnh gốc
contours, hierarchy = cv2.findContours(thresh3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(img3, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.rectangle(img_copy3, (x, y), (x+w, y+h), (0, 0, 255), 2)

# Hiển thị ảnh gốc với vùng khác biệt được khoanh đỏ


# Resize the image
resized_img1 = cv2.resize(img1, (new_width, new_height), interpolation = cv2.INTER_AREA)
resized_img_copy1 = cv2.resize(img_copy1, (new_width, new_height), interpolation = cv2.INTER_AREA)
vis1 = np.concatenate((resized_img1, resized_img_copy1), axis=1)

resized_img2 = cv2.resize(img2, (new_width, new_height), interpolation = cv2.INTER_AREA)
resized_img_copy2 = cv2.resize(img_copy2, (new_width, new_height), interpolation = cv2.INTER_AREA)
vis2 = np.concatenate((resized_img2, resized_img_copy2), axis=1)


resized_img3 = cv2.resize(img3, (new_width, new_height), interpolation = cv2.INTER_AREA)
resized_img_copy3 = cv2.resize(img_copy3, (new_width, new_height), interpolation = cv2.INTER_AREA)
vis3 = np.concatenate((resized_img3, resized_img_copy3), axis=1)

# cv2.imshow("Spot the Difference", vis1)
# cv2.imshow("Spot the Difference", vis2)
cv2.imshow("Spot the Difference", vis3)
cv2.waitKey(0)
cv2.destroyAllWindows()

