import os
import time

# image conversion
#os.system('python3 convert_images.py')

# eigennvalues
print("now running eigenvalue and svd recognition: loading...")
start = time.perf_counter()
os.system('python3 eigen/recognize_eigen.py')
end = time.perf_counter()
print(f"time elapsed: {end-start:.3f} seconds")

print()
print("********")
print()

# xgboost
print("now running xgboost tree recognition: loading...")
start = time.perf_counter()
os.system('python3 xgboost/recognize_xgboost.py')
end = time.perf_counter()
print(f"time elapsed: {end-start:.3f} seconds")

"""
graphing analysis
"""
"""
#os.system('python3 projects/art_facial_recognition/final/graph_accuracy.py')
"""