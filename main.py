import cv2
import os
import pandas as pd


image_files= 'file_path'

image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (00, 40)

# fontScale
fontScale = 1

# Red color in BGR
color = (255, 255, 255)

# Line thickness of 2 px
thickness = 2
image_files = [os.path.join(image_files, file) for file in os.listdir(image_files) if os.path.splitext(file)[1].lower() in image_extensions]

file_path = []
Annotated = []
Annotated_reason = []
current_image_index = 0

while (current_image_index<len(image_files)):
    current_image_path = image_files[current_image_index]
    image = cv2.imread(current_image_path)
    image = cv2.resize(image, (600, 600))
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.putText(image, str(current_image_index) + "/" + str(len(image_files)),org, font, fontScale,
                 color, thickness, cv2.LINE_AA, False)
    cv2.imshow("image",image,)
    key = cv2.waitKey(0)
    if key == 27:  # Esc key
        break
    elif key == ord("n"):
        file_path.append(image_files[current_image_index])
        Annotated.append('Fake')
        Annotated_reason.append('Nudity')
        current_image_index += 1
    elif key == 9: #tab key for next image
        current_image_index += 1
    elif key == ord("q"): #tab key for next image
        current_image_index -= 1
    elif key == ord("l"):
        file_path.append(image_files[current_image_index])
        Annotated.append('Fake')
        Annotated_reason.append('Lighting')
        current_image_index += 1
    elif key == ord("f"):
        file_path.append(image_files[current_image_index])
        Annotated.append('Fake')
        Annotated_reason.append('face not available')
        current_image_index += 1
    elif key == ord("p"):
        file_path.append(image_files[current_image_index])
        Annotated.append('Fake')
        Annotated_reason.append('photo of photo')
        current_image_index += 1
    elif key == ord("s"):
        file_path.append(image_files[current_image_index])
        Annotated.append('Fake')
        Annotated_reason.append('photo of screen')
        current_image_index += 1
    elif key == ord("r"):
        file_path.append(image_files[current_image_index])
        Annotated.append('Real')
        Annotated_reason.append('NA')
        current_image_index += 1
    cv2.destroyAllWindows()


Data = {
    'file_path' : file_path,
    'Annotated'  : Annotated,
    'Annotated_reason' : Annotated_reason
}

output = pd.DataFrame(Data)
print(output)
output.to_csv("New_data'.csv")
