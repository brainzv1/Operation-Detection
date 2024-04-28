Note:It looks better on code editor.

The data:
We’ve built an easy to use google drive folder to let those interested in the project check our findings and have a comfortable way to download the data into the project and run train for themself – here is the link:
https://drive.google.com/drive/folders/18_jo7MJhl6SVYaC9dXAN4p5ZIPyd0rQ1?usp=sharing

How to run
To execute the code, we created a conda environment named “openmmlab” (see ref) and used module load coda
Make sure you have torch. Run in terminal: pip list to see that you're compatible with us.
mmaction2 should be installed, make sure the filesToRun.py file we wrote is in the directory Operation-Detection and that the filesToRun folder contain all the files according to git.
Most of the files in the filesToRun folder will be executed by doing it terminal "python filesToRun.py", if you wish to change the TSN files to get different configurations for train and test they are also there.

Two files we haven't added to the input output questions of "filesToRun.py" are "classifyVideos.py" which created the demo folder that we uploaded to drive as "ClassifiedVideos"
and the "reduceDataSize.py" which helped us use ffmpeg to clear disk space due to our videos having heavy weight. you are invited to use those python files if you need.

We've added it to git but make sure to open a directory named “DataSet” in the “mmaction2” directory and inside it put the data under the directory “Data”.

Last but not least it is important that before you run train you change the code of the tsn file: manualOperationsProject\mmaction2\configs\recognition\tsn\tsn_imagenet-pretrained-r50_8xb32-1x1x3-100e_kinetics400-rgb.py
Entering the version from our source code will allow you to train and presumably achieve similar outcomes to what we had.
To process the data prior to training we created the filesToRun.py file which activates a series of the files we wrote ourselves to organize data.
If you followed all the instructions as follow you are supposed to be able to run the command in your terminal
python tools/train.py configs/recognition/tsn/tsn_imagenet-pretrained-r50_8xb32-1x1x3-100e_kinetics400-rgb.py

Notice: the train process is heavy on the GPU, and it uses a lot of resources from your computer, make sure to give it a lot of time to run.
You can also configure the number of epochs or other variables.
git repisotry for our code https://github.com/brainzv1/manualOperationsProject/edit/main/ReadMe.md
If there any problem here is the result of pip list using our conda env

We’ve created “mmaction2/commands.txt” so you can do train and test and other code usage from terminal the way you like from the project folder.

(openmmlab) [atamni@auth.ad.bgu.ac.il@dt-gpu-02 Operation-Detection]$ pip list
Package                  Version    Editable project location
------------------------ ---------- -------------------------------------------------------------------
absl-py                  2.0.0
addict                   2.4.0
aliyun-python-sdk-core   2.13.36
aliyun-python-sdk-kms    2.16.1
attrs                    23.1.0
brotlipy                 0.7.0
certifi                  2023.7.22
cffi                     1.15.1
charset-normalizer       2.0.4
chumpy                   0.70
click                    8.1.6
cmake                    3.27.0
colorama                 0.4.6
contourpy                1.1.0
crcmod                   1.7
cryptography             41.0.2
cycler                   0.11.0
Cython                   3.0.0
decorator                4.4.2
decord                   0.6.0
einops                   0.6.1
filelock                 3.9.0
flatbuffers              23.5.26
fonttools                4.42.0
gmpy2                    2.1.2
idna                     3.4
imageio                  2.31.1
imageio-ffmpeg           0.4.8
importlib-metadata       6.8.0
importlib-resources      6.0.0
Jinja2                   3.1.2
jmespath                 0.10.0
json-tricks              3.17.2
kiwisolver               1.4.4
lit                      16.0.6
Markdown                 3.4.4
markdown-it-py           3.0.0
MarkupSafe               2.1.1
matplotlib               3.7.2
mdurl                    0.1.2
mediapipe                0.10.7
mkl-fft                  1.3.6
mkl-random               1.2.2
mkl-service              2.4.0
mmaction2                1.1.0      /cs_storage/atamni/ServerBGU/Operation-Detection-MMAction/mmaction2
mmcv                     2.0.1
mmdet                    3.1.0
mmengine                 0.8.4
mmpose                   1.1.0
model-index              0.1.11
moviepy                  1.0.3
mpmath                   1.3.0
munkres                  1.1.4
networkx                 3.1
numpy                    1.24.3
nvidia-cublas-cu11       11.10.3.66
nvidia-cuda-cupti-cu11   11.7.101
nvidia-cuda-nvrtc-cu11   11.7.99
nvidia-cuda-runtime-cu11 11.7.99
nvidia-cudnn-cu11        8.5.0.96
nvidia-cufft-cu11        10.9.0.58
nvidia-curand-cu11       10.2.10.91
nvidia-cusolver-cu11     11.4.0.1
nvidia-cusparse-cu11     11.7.4.91
nvidia-nccl-cu11         2.14.3
nvidia-nvtx-cu11         11.7.91
opencv-contrib-python    4.8.0.74
opencv-python            4.8.0.74
opendatalab              0.0.10
openmim                  0.3.9
openxlab                 0.0.17
ordered-set              4.1.0
oss2                     2.17.0
packaging                23.1
pandas                   2.0.3
Pillow                   9.4.0
pip                      23.2.1
platformdirs             3.10.0
proglog                  0.1.10
protobuf                 3.20.3
pycocotools              2.0.6
pycparser                2.21
pycryptodome             3.18.0
Pygments                 2.15.1
pyOpenSSL                23.2.0
pyparsing                3.0.9
PySocks                  1.7.1
python-dateutil          2.8.2
pytz                     2023.3
PyYAML                   6.0.1
requests                 2.28.2
rich                     13.4.2
scipy                    1.10.1
setuptools               60.2.0
shapely                  2.0.1
six                      1.16.0
sounddevice              0.4.6
sympy                    1.11.1
tabulate                 0.9.0
termcolor                2.3.0
terminaltables           3.1.10
tomli                    2.0.1
torch                    2.0.1
torchaudio               2.0.2
torchvision              0.15.2
tqdm                     4.65.0
triton                   2.0.0
typing_extensions        4.7.1
tzdata                   2023.3
urllib3                  1.26.16
wheel                    0.38.4
xtcocotools              1.13
yapf                     0.40.1
zipp                     3.16.2
(openmmlab) [atamni@auth.ad.bgu.ac.il@dt-gpu-02 Operation-Detection]$
