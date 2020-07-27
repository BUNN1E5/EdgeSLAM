# SLAM Implementation

In an effort to learn more about OpenCV I am making an attemped at writing a custom implementation of the SLAM algorithm

## TODO 

Basically Everything 0.o

## About this implementation

This is will be a single camera implementation of SLAM as I only have a single PS3 Eye camera right now. 

Here are some ideas about the high level on how this algorithm is going to determine position

Using ORB Feature matching we can actually compare between 2 different images, the current frame and the previous
this should give us a basic idea about the opitcal flow of our camera by finding the average distance moved between frames.

This isn't perfect however, becasue there is the possibility of moving objects within the frame. So we also have to remove any outlier
or weigh the different points by some measure.


Now there is also the problem that this method does not find any rotational movement, which is unfortunate, but as of right now I want to get this basic motion detection working.

### Potential Ideas

Can we use an edge detection algorithm to make it easier to find keypoints as well as remove a lot of noise?

## Resourses
Apparntly Kalman filter is pretty important
https://medium.com/@jannik.zuern/robot-localization-with-kalman-filters-and-landmarks-cf97fa44e80b
Seems like a good article?

Also looks pretty usefull
https://atsushisakai.github.io/PythonRobotics/#slam
and
https://github.com/jzuern/robot-localization

Data structure to store the datapoints
https://answers.ros.org/question/331731/data-structure-to-store-a-map-while-doing-it-with-slam/

