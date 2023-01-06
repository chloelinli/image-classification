import os

# image conversion
os.system('python3 projects/art_facial_recognition/final/image_to_csv.py')
os.system('python3 projects/art_facial_recognition/final/image_to_csv_E.py')
os.system('python3 projects/art_facial_recognition/final/image_to_csv_H.py')

# image reconstruction
os.system('python3 projects/art_facial_recognition/final/reconstruct_images.py')

# image recognition
os.system('python3 projects/art_facial_recognition/final/recognize_images.py')