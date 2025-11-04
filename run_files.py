import os
import time

# image conversion
#os.system('python3 convert_images.py')

# ensure labels
os.system('python3 update_labels.py')

print()
print("********")
print()

# eigennvalues
print("now running eigenvalue and svd classification: loading...")
start = time.perf_counter()
os.system('python3 eigen/eigen.py')
end = time.perf_counter()
print(f"time elapsed: {end-start:.3f} seconds")

print()
print("********")
print()

# xgboost
print("now running xgboost tree classification: loading...")
start = time.perf_counter()
os.system('python3 xgboost/xgboost.py')
end = time.perf_counter()
print(f"time elapsed: {end-start:.3f} seconds")

print()
print("********")
print()

# k-nearest neighbors
print("now running k-nearest neighbors classification: loading...")
start = time.perf_counter()
os.system('python3 knn/knn.py')
end = time.perf_counter()
print(f"time elapsed: {end-start:.3f} seconds")

# graph analysis
os.system('python3 results/graph_accuracy.py')