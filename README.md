<h1 align="center">Facebook's Detectron2 Windows 10 Demo</h1>
This repo contains the process of getting started with Facebook FAIR's detectron2 project on windows 10 without any Nvidia GPU.
<a href="#">
  <div align="center">
    <img src="images/segmented_image.jpg" width='700'/>
  </div>
</a>

## Configuration and Installation steps

To install Detectron2 you need to have Pytorch and Torchvision installed along with Pycocotools.

To install Pycocotools On Windows, you must have the Visual C++ 2015 build tools on your path. If you don't, make sure to install them from [here](https://go.microsoft.com/fwlink/?LinkId=691126):

Then, run `visualcppbuildtools_full.exe` and select default options:

After installing add them to your environment variables and run the command below:
```
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
```
This will install pycocotools into your opreating system.

After that install the requirements specified in the requirement file.
```
pip install -r requirement.txt
```

To build the Detectron2 you need fvcore 
```
git clone https://github.com/facebookresearch/detectron2.git
cd detectron2 && pip install -e .
```
When all the requirements are installed clone the official repository of Detectron2 project from [here](https://github.com/facebookresearch/detectron2)
or you can clone it by the process given below
```
git clone https://github.com/facebookresearch/detectron2.git
cd detectron2
python setup.py build develop
```
After doing that all you need are pretrained models and pretrained weights.

You can get pre trained Mask RCNN model from [here](https://mega.nz/#!0nhxGKSA!GUOEjejGvy5sU5MZa8TFZUY0r4VT5al4Y_q0jZSiXW0) and pre trained weights from [here](https://mega.nz/#!cnZkQazC!Qp25xoks1OShLnXk_kIA6oniJ3q_yj7NYCU4fnZGRBs)
Place these models and weights in the working directory of the python script.

At Last you need to download the Base RCNN model from [here](https://mega.nz/#!xmAElA7A!fOHCnMQh6WzO1mcmktpyDh5D16AmqgC4fYp3tNwye_4)
and you need to place this file out of the current working directory in the previous directory to use this base model.

After configuring this just run the python script given in the code put your image name or path in the script and run this.
# Enjoy

----------------------------------------------------------------------------------------------------------------------------------------


## Author
You can get in touch with me on my LinkedIn Profile:

#### Saad Hassan
[![LinkedIn Link](https://img.shields.io/badge/Connect-saadhaxxan-blue.svg?logo=linkedin&longCache=true&style=social&label=Connect
)](https://www.linkedin.com/in/saadhaxxan)

You can also follow my GitHub Profile to stay updated about my latest projects: [![GitHub Follow](https://img.shields.io/badge/Connect-saadhaxxan-blue.svg?logo=Github&longCache=true&style=social&label=Follow)](https://github.com/saadhaxxan)

If you liked the repo then kindly support it by giving it a star ⭐!

## Contributions Welcome
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](#)

If you find any bug in the code or have any improvements in mind then feel free to generate a pull request.

## Issues
[![GitHub Issues](https://img.shields.io/github/issues/saadhaxxan/Detectron2_Demo_Windows_10.svg?style=flat&label=Issues&maxAge=2592000)](https://www.github.com/saadhaxxan/Detectron2_Demo_Windows_10/issues)

If you face any issue, you can create a new issue in the Issues Tab and I will be glad to help you out.

## License
[![MIT](https://img.shields.io/cocoapods/l/AFNetworking.svg?style=style&label=License&maxAge=2592000)](../master/LICENSE)

Copyright (c) 2019 SAAD HASSAN   
