# README !!

### Step 1: 	
Check the python version (it should be 3.7)
```
python --version
>>Python 3.7.0
```

### Step 2:
download and install cmake (*add to path) https://cmake.org/download/
```
cmake --version
```

### Step 3:	
clone the repo in C:\src\vcpkg or C:\dev\vcpkg (recommended path to access it globally)
```
C:\src>git clone https://github.com/microsoft/vcpkg
```
```
C:\src>.\vcpkg\bootstrap-vcpkg.bat
```

### Step 4:
In order to use vcpkg with Visual Studio, run the following command (may require administrator elevation):
```
C:\src>.\vcpkg\vcpkg integrate install 
C:\src>./vcpkg.exe install ffmpeg:x64-windows 	or
C:\src>./vcpkg.exe install ffmpeg --triplet=x64-windows
```
(just for reference: https://trac.ffmpeg.org/wiki/CompilationGuide/vcpkg)

### Step 5
once ffmpeg is installed go to:
```
src\vcpkg->installed->x64-windows->include->libavcodec 
and replace the avcodec file with the one provided
```

### Step 6:	
clone the h264decoder in you project folder
```
git clone https://github.com/DaWelter/h264decoder.git
```
Change the version of pybind to 2.8.1 in CMakelist.txt:	
```
find_package(pybind11)
	......
	GIT_REPOSITORY https://github.com/pybind/pybind11
	GIT_TAG v2.8.1)
	......
```

### Step 7:
in cmd redirect to the folder's location
create a build folder in it (mkdir build or you can manually build it)
(this is a manual method which i used)	
```
cmake -DCMAKE_TOOLCHAIN_FILE=[path to vcpkg folder]/scripts/buildsystems/vcpkg.cmake -A x64 ..
```
```
cd build
```
```
cmake -DCMAKE_TOOLCHAIN_FILE=C:/src/vcpkg/scripts/buildsystems/vcpkg.cmake -A x64 ..
```
```
cmake --build .
```
OR
else directly build it using: (setup.py already exists in the folder)
```	
python setup.py build_ext --cmake-args="-DCMAKE_TOOLCHAIN_FILE=[path to vcpkg folder]/scripts/buildsystems/vcpkg.cmake"	
```
```
pip install -e.
```
