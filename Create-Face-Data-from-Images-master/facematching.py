import os
import shutil
import face_recognition
base_dir = os.path.dirname(__file__)
known_image = face_recognition.load_image_file("faces\\0_mess2.jpg")
input_img_encoding = face_recognition.face_encodings(known_image)[0]
for file in os.listdir(base_dir + 'faces'):

    unknown_image = face_recognition.load_image_file(base_dir+"faces/"+file)
    try:
        output_img_encoding = face_recognition.face_encodings(unknown_image)[0]
    except IndexError as e:
        print(e)
    # print(type(output_img_encoding))
    results = face_recognition.compare_faces([input_img_encoding], output_img_encoding)
    print(results)
    if results[0]==True:
        temp_name=file.partition("_")[2]
        if not os.path.exists('extracted_photos'):
	        print("New directory created")
	        os.makedirs('extracted_photos')
        shutil.copy(base_dir +"images/"+temp_name, base_dir+"extracted_photos/")