# pyffc

Do flat field correction and histogram equalization. Used in particular on photos where vignette appears.

1. Select some photos to use for generating a mask, place these in a folder: \mask\*.jpg
2. Run script to generate mask, it will additively blend the images
3. Place photos of interest inside another folder and modify script to work on those (need to confirm batch work behaviour)
4. Output is ffc, as well as ffc+clahe. Clahe can be tuned with clip_limit parameter.

![alt text](https://github.com/joakimsk/pyffc/blob/main/sample/sample.jpg?raw=true)

![alt text](https://github.com/joakimsk/pyffc/blob/main/sample/sample_ffc_clahe.jpg?raw=true)
