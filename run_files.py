import os

# image conversion
"""
os.system('python3 projects/art_facial_recognition/final/image_to_csv.py')
os.system('python3 projects/art_facial_recognition/final/image_to_csv_E.py')
os.system('python3 projects/art_facial_recognition/final/image_to_csv_M.py')
os.system('python3 projects/art_facial_recognition/final/image_to_csv_H.py')
"""

# eigen - image reconstruction
"""
os.system('python3 projects/art_facial_recognition/final/results/reconstruct_eigen.py')
"""

"""
image recognition
"""
# eigen
os.system('python3 projects/art_facial_recognition/final/results/recognize_eigen.py')

# xgboost
os.system('python3 projects/art_facial_recognition/final/results/recognize_xgboost.py')

"""
graphing analysis
"""
#os.system('python3 projects/art_facial_recognition/final/graph_accuracy.py')