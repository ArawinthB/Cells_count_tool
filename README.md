# Cells_count_tool
Following a need for image analysis in the context of cells detection, this project was created. 
This script was writted in python 3.8.

The tool count each cells on a .jpg file. It works with a black background on the jpg.

1. Load a .jpg file
2. Two pictures will appear. Left image is the original picture. Right image present what the tool detect on the picture (white object). This firts analyze is based with a threshold value at 20.
3. In the new windows you will see the results summary :
     - Filename 
     - Save directory
     - Number of cells count
     - Threshold Value

4. At this step, if the number of cells count is okay for you can leave, otherwise you can update the threshold value and it will refresh the analyze & cells count number.
