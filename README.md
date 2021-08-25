# Cells_count_tool
v1.2
Following a need for image analysis in the context of cells detection, this project was created with the Lund University. 
This script was writted in python 3.8.

The tool count each cells on a .jpg/.png/.tiff file. 

1. Load a file
2. Two pictures will appear. Left image is the original picture, windows call "Original picture". 
   Right image present what the tool detect on the picture (white object), windows call "contour_detected_image". 
   This firts analyze is based with a threshold value at 20.
4. In the new windows you will see the results summary :
     - Filename 
     - Save directory
     - Number of cells count
     - Threshold Value
4. At this step, if the number of cells count is okay for you can leave, otherwise you can update the threshold value and it will refresh the analyze & cells count number.


# Multiple_cells_count.py
You can have a fast analyse of many picture in same folder, with this python script. 

1. Put the Multiple_cells_count.py in the same folder of your others pictures files.
2. Run the script with Spyder or another python environment.
3. Discover your result in the "PYCELL.xlsx" excel file.

You can change the threshold in the script, at the "if__name__ ='__main___':" level (l.188).
