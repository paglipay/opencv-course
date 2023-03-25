https://www.youtube.com/watch?v=P-EZr0zy53g
List of commands:

sudo apt-get install python3-pip 
pip3 install virtualenv 
python3 -m virtualenv -p python3 env --system-site-packages    
source env/bin/activate 
python -c 'import cv2; print(cv2.__version__)' 

Create SwapFile:
sudo fallocate -l 4G /var/swapfile 
sudo chmod 600 /var/swapfile
 sudo mkswap /var/swapfile
 sudo swapon /var/swapfile
 sudo bash -c 'echo "/var/swapfile swap swap defaults 0 0"  >> /etc/fstab’ 

Reboot your PC: sudo reboot
After rebooting check swap space  by using this command:   free -h

Install these Dependencies before installing OpenCV:

sudo sh -c "echo '/usr/local/cuda/lib64' >> /etc/ld.so.conf.d/nvidia-tegra.conf“
sudo ldconfig
sudo apt-get install build-essential cmake git unzip pkg-config
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install libgtk2.0-dev libcanberra-gtk*
sudo apt-get install python3-dev python3-numpy python3-pip
sudo apt-get install libxvidcore-dev libx264-dev libgtk-3-dev
sudo apt-get install libtbb2 libtbb-dev libdc1394-22-dev
sudo apt-get install libv4l-dev v4l-utils
sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
sudo apt-get install libavresample-dev libvorbis-dev libxine2-dev
sudo apt-get install libfaac-dev libmp3lame-dev libtheora-dev
sudo apt-get install libopencore-amrnb-dev libopencore-amrwb-dev
sudo apt-get install libopenblas-dev libatlas-base-dev libblas-dev
sudo apt-get install liblapack-dev libeigen3-dev gfortran
sudo apt-get install libhdf5-dev protobuf-compiler
sudo apt-get install libprotobuf-dev libgoogle-glog-dev libgflags-dev

Download OpenCV:
cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.1.zip 
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.5.1.zip 
unzip opencv.zip 
unzip opencv_contrib.zip

Now rename the directories. Type each command below, one after the other.
mv opencv-4.5.1 opencv
mv opencv_contrib-4.5.1 opencv_contrib
rm opencv.zip
rm opencv_contrib.zip

Lets build OpenCV now:
cd ~/opencv
mkdir build
cd build 


copy and paste this entire block of commands below into your terminal.

cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules -D EIGEN_INCLUDE_PATH=/usr/include/eigen3 -D WITH_OPENCL=OFF -D WITH_CUDA=ON -D CUDA_ARCH_BIN=5.3 -D CUDA_ARCH_PTX="" -D WITH_CUDNN=ON -D WITH_CUBLAS=ON -D ENABLE_FAST_MATH=ON -D CUDA_FAST_MATH=ON -D OPENCV_DNN_CUDA=ON -D ENABLE_NEON=ON -D WITH_QT=OFF -D WITH_OPENMP=ON -D WITH_OPENGL=ON -D BUILD_TIFF=ON -D WITH_FFMPEG=ON -D WITH_GSTREAMER=ON -D WITH_TBB=ON -D BUILD_TBB=ON -D BUILD_TESTS=OFF -D WITH_EIGEN=ON -D WITH_V4L=ON -D WITH_LIBV4L=ON -D OPENCV_ENABLE_NONFREE=ON -D INSTALL_C_EXAMPLES=OFF -D INSTALL_PYTHON_EXAMPLES=OFF -D BUILD_NEW_PYTHON_SUPPORT=ON -D BUILD_opencv_python3=TRUE -D OPENCV_GENERATE_PKGCONFIG=ON -D BUILD_EXAMPLES=OFF ..


Build OpenCV. This command below will take a long time (around 2 hours), make -j4     # (make then space single dash and then j4)

Finish the install:
cd ~
sudo rm -r /usr/include/opencv4/opencv2
cd ~/opencv/build
sudo make install
sudo ldconfig
make clean
sudo apt-get update 

Verify OpenCV Installation
#open python3 shell
python3
import cv2
cv2._version_


Install jtop, a system monitoring software for Jetson Nano.
cd ~
sudo -H pip3 install -U jetson-stats 
sudo reboot
jtop


Test Your Camera on Jetson Nano:
Turn on your Jetson Nano.
Open a new terminal window, and type:
ls /dev/video0   #csi camera
ls /dev/video*   # show you a list of cameras

Take a Photo:
nvgstcapture-1.0 --orientation=2       # for testing CSI camera
# V4L2 USB camera 
nvgstcapture-1.0 --camsrc=0 --cap-dev-node=1

git config --global user.name "Paul Aglipay"
git config --global user.email "paglipay@gmail.com"

sudo pip3 install adafruit-circuitpython-servokit

sudo pip3 install --upgrade pip
sudo pip3 install opencv-python==4.5.1.48
sudo pip3 install --upgrade opencv-python

sudo apt install libpython3.7-dev

wget http://dlib.net/files/dlib-19.23.tar.bz2
tar jxvf dlib-19.23.tar.bz2
cd dlib-19.23/
mkdir build
cd build/
cmake ..

cmake --build .
cd ../
sudo python3 setup.py install
sudo pip3 install face_recognition
