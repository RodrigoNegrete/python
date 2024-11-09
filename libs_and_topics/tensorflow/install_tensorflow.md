# requisite table
https://www.tensorflow.org/install/source#gpu

# install tensorflow in windows
https://www.youtube.com/watch?v=hHWkvEcDBO0&t=336s

# install with anaconda in windows
https://www.youtube.com/watch?v=5Ym-dOS9ssA&list=PLhhyoLH6IjfxVOdVC1P1L5z5azs0XjMsb&index=1


# How to run Tensorflow using NVIDIA CUDA and Docker on Windows 10 WSL ?
https://www.datalearnings.com/how-to-run-tensorflow-using-nvidia-cuda-and-docker-on-windows-wsl/


# Installation
## Pre Requiesites for GPU
1. python 3.7 - 3.9 https://www.python.org/downloads/windows/
2. NVIDIA Drivers - run as admin. https://www.nvidia.com/download/index.aspx?lang=en-us
3. Visual Studio 2019 - run as admin.- https://download.visualstudio.microsoft.com/download/pr/8e9dbf43-d1e3-495c-b03d-7178db3fc365/5c1dca106a963f60dc71a1a6e0cd2735/vs_community.exe
4. Install cuda 11.2 -r run as admin. https://developer.nvidia.com/cuda-toolkit-archive
5. Install cudnn 8.1 - run as admin. https://developer.nvidia.com/rdp/cudnn-download
    1. Go to Downloaded Folder
    2. Copy bin, include and lib
    3. Go to Program Files/NVidia GPU Computing Toolkit/CUDA/Version
    4. Paste and replace
    5. Copy Location of bin folder
    6. Go to environmental Variables - Path - Edit - New
    7. Paste bin location 
    8. Copy Location of libnvvp folder
    9. Go to environmental Variables - Path - Edit - New
    10. Paste bin location 
6. Restart Computer

## install Tensorflow 
- Tensorflow 2.7