## Running files
If you are struggling to run the files properly on your own system due to "No such file or directory" or similar errors, you may have to modify the paths in the following files:

```run_files.py```
```image_to_csv.py```
```reconstruct_images.py```

## Training
In order to run the scripts that reconstruct the converted images, you must install matplotlib.

```pip install matplotlib```

If you are wanting to use similar code in the reconstruction file, thegenfromtxt method will not work if your images are not of dimension `n x n`. The given code assumes pictures of size 300x300, so if you have not sized your images as such, you will have to manually change the dimension variables `h, w` in the following files, if you plan to use them:

```image_to_csv.py```
```reconstruct_images.py```