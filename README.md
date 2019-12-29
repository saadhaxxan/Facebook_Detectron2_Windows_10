<h1 align="center">Facebook's Detectron2_Demo_Windows_10</h1>
This repo contains the process of getting started with Facebook FAIR's detectron2 project on windows 10 without any Nvidia GPU.
<a href="#">
  <div align="center">
    <img src="images/segmented_image.jpg" width='700'/>
  </div>
</a>

## Configuration and Installation steps

First install Detectro2 on your local machine and to install Detectron2 you need to have Pytorch and Torchvision installed along with Pycocotools.

To install Pycocotools On Windows, you must have the Visual C++ 2015 build tools on your path. If you don't, make sure to install them from [here](https://go.microsoft.com/fwlink/?LinkId=691126):

Then, run `visualcppbuildtools_full.exe` and select default options:

After installing add them to your environment variables and run the command below:
```
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
```


