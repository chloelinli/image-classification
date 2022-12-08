## Running files
If you are struggling to run the files properly on your own system due to "No such file or directory" or similar errors, you may have to modify the paths in the following files:

```run_files.py```
```image_to_csv.py```

## Training
In order to run the scripts that reconstruct the converted images, you must install matplotlib.

```pip install matplotlib```

If you are wanting to use similar code in the reconstruction file, thegenfromtxt method will not work if your images are not the same size in terms of pixels. My pictures are 300x300 pixels, so I initialized height and width as 300 in the following code snippet:

```
path = 'projects/art_facial_recognition/data'

# load data
data = np.genfromtxt(path+'/train_images_small_test.csv', delimiter=',')
h = 300
w = 300
```