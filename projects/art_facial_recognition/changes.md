### 2.1.0
* Updated init and unrel character accuracy values with XGBoost [#37531eb](https://github.com/chloelinli/chloelinli.github.io/commit/37531eb07b629a6799f3ba63068e5f562321ee9b)
* Updated graph script to accomodate 2 unrelated characters per difficulty using subplots [#ae89cba](https://github.com/chloelinli/chloelinli.github.io/commit/ae89cba219d1aa4a9df2218320b6b78d1511e338)

### 2.0.0
* Created XGBoost from scratch script as another machine learning algorithm for facial recognition [#c8ba2c7](https://github.com/chloelinli/chloelinli.github.io/commit/c8ba2c72cb84650f5802b20384683a0bbad785c9)
* Updated accuracy list with XGBoost values [#e3a9f1a]([https://github.com/chloelinli/chloelinli.github.io/commit/e3a9f1a9b77f42a7d4be1f82fdbb0fd9e845c427)

### 1.2.0
* Created script to graph accuracy of different recognition methods [#89a980b](https://github.com/chloelinli/chloelinli.github.io/commit/89a980bc96c348caf0df42a6d018b65404552ae)
* Renaming in graph from Eigen to SVD [#d9cc1ce](https://github.com/chloelinli/chloelinli.github.io/commit/d9cc1ce468e6189ff90c5e21291d9f6fc3555027)
* Adjusted y-axis of graph to account for readability [#5adfcf3](https://github.com/chloelinli/chloelinli.github.io/commit/5adfcf332764ec249cdfc9682eb0f1021dd8a7d1)

### 1.1.5
* Added column header to eigen/SVD method in the accuracy file [#938c65f](https://github.com/chloelinli/chloelinli.github.io/commit/938c65fc9b8a553e1cedbf20f177640b3095fd3d)
* Moved and renamed files related to SVD and eigenvector scripts [#b5213f0](https://github.com/chloelinli/chloelinli.github.io/commit/b5213f037c30f8b66fe7f209172a2c96d1b5a4f0)

### 1.1.4
* Modified eigen/SVD script to account for less lines in main method and exporting accuracy values to csv [#1fbe1e6](https://github.com/chloelinli/chloelinli.github.io/commit/1fbe1e61553e393f9fe3850c648040205d0130c1)

### 1.1.3
* Reformatting eigen accuracy print message, prepared run files script for future methods [#23fa828](https://github.com/chloelinli/chloelinli.github.io/commit/23fa82847ed50567acc28a805f9061746aac0132)

### 1.1.2
* Moved and renamed files due to LFS [#b5213f0](https://github.com/chloelinli/chloelinli.github.io/commit/b5213f037c30f8b66fe7f209172a2c96d1b5a4f0)
* Readjusting LFS [#9218601](https://github.com/chloelinli/chloelinli.github.io/commit/9218601e5e7ecce29f80b572dbb9b3f22595e07e), [#a0c60ee](https://github.com/chloelinli/chloelinli.github.io/commit/a0c60ee1ea1585e0d87efd5b2e710029cdd0cc46)


### 1.1.1
* Removed accuracy files containing manual entries [#96f4beb](https://github.com/chloelinli/chloelinli.github.io/commit/96f4bebe90642482d529bfb7eb583bbca2cb3dbd), [#5b3de42](https://github.com/chloelinli/chloelinli.github.io/commit/5b3de426b9bd4bd6a45d84c7ebef2040979797e4), [#543b3a1](https://github.com/chloelinli/chloelinli.github.io/commit/543b3a1ed0d5fa238ce6d71af9a554e2063f9315)

### 1.1.0
* Added directories and renamed files to distinguish method [#fe4a69a](https://github.com/chloelinli/chloelinli.github.io/commit/fe4a69ac922d1869af90b76ca8c7815392dda3c9), [#9e3416d](https://github.com/chloelinli/chloelinli.github.io/commit/9e3416d3956c33a8447d93c468bc425bbcc73a3a), [#1e65319](https://github.com/chloelinli/chloelinli.github.io/commit/1e65319cb9d43f73c5dce686bf48c52086341be8)

### 1.0.2
* Updated SVD values in comment to corresponding k_90 and k_99 with new data [#5e63323](https://github.com/chloelinli/chloelinli.github.io/commit/5e63323524a05b6e34df48574cef1730f929d2af)

### 1.0.1
* Added functions to image conversion file to be able to work with several different directories instead of using specific values [#6185119](https://github.com/chloelinli/chloelinli.github.io/commit/6185119cb78cb441e8ab8320f2aa63f91aa9acf3)
* Added file holding commands to run all files easily [#e0a9b3d](https://github.com/chloelinli/chloelinli.github.io/commit/e0a9b3d6bd09f73703badd96015ea02615354fb0)
* Added variables for dimensions to allow for modifications [#5071141](https://github.com/chloelinli/chloelinli.github.io/commit/507114169eec76316ec40558cdc549633deeb850)
* Updated reconstructed images with SVDs in small test [#e2938f4](https://github.com/chloelinli/chloelinli.github.io/commit/e2938f40c7dd2e377889a1630cb1c3d0ae882646)
* Included plots of SVDs and their scaled energies [#8ae7166](https://github.com/chloelinli/chloelinli.github.io/commit/8ae71661fee4e8495c86c62fa1ff6a6bcde0f1a5)
* Added accuracy of reconstruction to final file [#db3655a](https://github.com/chloelinli/chloelinli.github.io/commit/db3655a56ade42cb1864f45ec3c6afd8f4ac32e9)
* Fixed image conversion by adding second file [#e0e62a6](https://github.com/chloelinli/chloelinli.github.io/commit/e0e62a6b92d07539b0cbdaf60221401dd7c9202f)
* Added V values from SVD to csvs for future use [#bafcd0e](https://github.com/chloelinli/chloelinli.github.io/commit/bafcd0e39cfdfdfb5403d52f3765b26f3c078df2), [#a0572ad](https://github.com/chloelinli/chloelinli.github.io/commit/a0572ad467105e241c27cfe75c278126316c2209})
* Added unrelated characters to training images [#1337f54](https://github.com/chloelinli/chloelinli.github.io/commit/1337f54d42fc2a71120dbbb98a10f84b88154131), [#7080abd](https://github.com/chloelinli/chloelinli.github.io/commit/7080abd6e8a98273a309da6955b65ba8d41fee41)

### 1.0.0
#### Small test
* Initial image_to_csv and reading csv test files [#fb28981](https://github.com/chloelinli/chloelinli.github.io/commit/fb28981574fa34efb51a112e612fa79f00df246a)
* Training [#605c41e](https://github.com/chloelinli/chloelinli.github.io/commit/605c41e1edce468c01b31299790923e9c23b832e)
* Converted from RGB to grayscale in image_to_csv to make reconstruction easier [#063b914](https://github.com/chloelinli/chloelinli.github.io/commit/063b914afedf4c373a45ca1c002579701352a384)