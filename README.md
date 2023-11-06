# COM Tracker
Tracks the centre of mass of an object over time

### Conda
```
conda create --name
conda activate centtr
conda install numpy
conda install matplotlib
conda install opencv-python
conda install ipykernel
```

### Openpose
- use OpenPose v1.6.0
- download the models by running the batch file
- Most code taken from: https://learnopencv.com/deep-learning-based-human-pose-estimation-using-opencv-cpp-python/ and https://github.com/spmallick/learnopencv/blob/master/OpenPose/OpenPoseImage.py
- add folder `./models` contains the following files: https://github.com/CMU-Perceptual-Computing-Lab/openpose/tree/master/models
- different output formats: https://cmu-perceptual-computing-lab.github.io/openpose/web/html/doc/md_doc_02_output.html#pose-output-format-body_25

### For Center of Gravity:
- https://www.sportsbiomech.com/Books/Human%20Body%20Dynamics%20-%20classical%20mechanics%20and%20human%20movement.pdf, page 20 (Chrome PDF viewer)
> The biggest part of the human body is
the trunk; comprising on the average 43% of total body weight. Head and
neck account for 7% and upper limbs 13% of the human body by weight.
The thighs, lower legs, and feet constitute the remaining 37% of the total
body weight

### Misc
- Image reading code taken from: https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/

### Todo
- Rename to center of gravity tracker
