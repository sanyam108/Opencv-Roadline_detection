{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7476b30c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0a78c057",
   "metadata": {},
   "outputs": [],
   "source": [
    "video =cv2.VideoCapture(\"road_car_view.mp4\")\n",
    "\n",
    "while True:\n",
    "    ret,or_frame=video.read()\n",
    "    if not ret :\n",
    "        video =cv2.VideoCapture(\"road_car_view.mp4\")\n",
    "        continue\n",
    "    frame=cv2.GaussianBlur(or_frame,(5,5),0)\n",
    "    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)\n",
    "    \n",
    "    lower_y=np.array([18,94,140])\n",
    "    upper_y=np.array([48,255,255])\n",
    "    \n",
    "    mask=cv2.inRange(hsv,lower_y,upper_y)\n",
    "    edges=cv2.Canny(mask,74,150)\n",
    "    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)\n",
    "    if lines is not None:\n",
    "        for line in lines:\n",
    "            x1,y1,x2,y2 = line[0]\n",
    "            cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)\n",
    "    \n",
    "    cv2.imshow(\"frame\",frame)\n",
    "    cv2.imshow(\"edges\",edges)\n",
    "\n",
    "    if cv2.waitKey(2) & 0xFF == ord('q'):\n",
    "            break \n",
    "    \n",
    "    \n",
    "video.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3294f06",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
