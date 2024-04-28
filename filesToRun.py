import subprocess
import sys

#Welcome message
print("\nHello! Welcome to our file distribution setup \n\n To begin you should make sure and you have the data we've assembled download to mmaction2/DataSet/Data \n If you don't have it you should download it from https://drive.google.com/drive/folders/1xjbNzlf0g6sHw7ZENqcqKJOS0h3spoMz?usp=drive_link\n")
#maybe add before we start with questions are the files there? if yes code continue if no ask if download for them and code that downloads
#Choose file handling system.
print("\nFirst question! in which way would you be interested to train your data? \n 1.Distributed VideoDataSet \n 2.RawFrameDataSet\n 3.VideoDataSet without distribution (not recommended due to no distinct folders for train, test and validation)")
while True:
    try:
        method = int(input())
        if method == 1 or method == 2 or method == 3:
            break
        else:
            print("Please enter the value 1 or 2 or 3.")
    except ValueError:
        print("Please enter a valid integer.")
    except NameError:
        print("Please enter a valid integer.")

#add reduce data size using ffmpeg question? code in folder filesToRun need to check if it works


#To determine if delete the data in case it is not needed for train test and val
#maybe add option/followup question of unzip and zip videos and files during run for less disk but no delete? it might be question that suits also option 3 of method
if (method == 1 or method == 2):
    print("\nAnother question! Would you like to keep the data in DataSet/Data for the next time you run filesToRun.py? \n 1.Delete the data to prevent disk usage \n 2.Keep the data for future use")
    while True:
        try:
            keepData = int(input())
            if keepData == 1 or keepData == 2:
                break
            else:
                print("Please enter a the value  1 or 2.")
        except ValueError:
            print("Please enter a valid integer.")
        except NameError:
            print("Please enter a valid integer.")
    #both extractRawFrames and extractVideo should get keepdata as args to determine if delete
#for rawframe creation,important for size of data
if method == 2:
    print("\nWhat estimated % of all frames do you want to keep? Note that this affects disk space and duration of train \nit is very important that you have time and disk space if you go with high %\nPlease enter a number:")
    while True:
        try:
            user_input = int(input())
            if 0 < user_input <= 100:
                skip_probability = 0.01 * user_input
                break
            else:
                print("Please enter a value between 1 and 100.")
        except ValueError:
            print("Please enter a valid integer.")
        except NameError:
            print("Please enter a valid integer.")


print("Our code is running now, this might take a while \nwe will write here again when its finished")
#The following code will activate files in order according to correct method and will pass important variables.

# Define the list of Python files you want to run in order
#Again works only if you're cd to the project itself dir
files_to_run = ["filesToRun/createAno.py"]
if method == 1:
    files_to_run.extend(["filesToRun/distributeData.py", "filesToRun/videoDataSet/extractVideos.py"])
if method == 2:
    files_to_run.extend(["filesToRun/distributeData.py", "filesToRun/rawFrameDataSet/extractRawFrames.py", "filesToRun/rawFrameDataSet/reorganizeData.py"])

# Loop through the list and run each script sequentially
for script in files_to_run:
    value = ''
    value2 = ''
    if script == "filesToRun/rawFrameDataSet/extractRawFrames.py":
        value = str(skip_probability)
        value2 = str(keepData)
    if script == "filesToRun/videoDataSet/extractVideos.py":
        value = str(keepData)
    if script == "filesToRun/createAno.py":
        value = str(method)
    subprocess.run(["python", script, value, value2], check=True)

#Old code when had only one method - important for understanding flow of ACTIONS in each on of the if statements
# Define the list of Python files you want to run in order
#files_to_run = ["createAno.py", "distributeData.py", "extractRawFrames.py", "reorganizeData.py"]

# Loop through the list and run each script sequentially
#for script in files_to_run:
#    subprocess.run(["python", script], check=True)
#Notice: the extractRawFrames.py file takes a lot of time, especially when all frames are captures.
#In order to make a shorter run time you might want to switch to VideoDataset (config) format and use the mp4 files.
#Instructions how to train
print("All done! now you are ready to train, test and do whatever you like! \n this is where we leave you to do as you please but here is how you should run train and test\n simply put in your console: \n incase of VideoDataSet: python mmaction2/tools/train.py filesToRun/videoDataSet/videoDataSetTSNFile.py \n incase of RawFrameDataSet: python mmaction2/tools/train.py filesToRun/rawFrameDataSet/rawframesTSNFile.py \n incase of undistributed VideoDataSet: python mmaction2/tools/train.py filesToRun/videoDataSet/unDistributedVideoDataSetTSNFile.py \n NOTE: this relies on you being in the directory of the project so make sure you use cd to get to the right place")
print("\nNOTICE: If you are having space problems or disk quota exceeded problems go to mmaction2/DataSet/Data \n The data folder should be deleted if specified to do so but the train,test and val have to deleted manually if needed\n")
#Add instructions how to test once you know how!
print("After you finished training its testing time")

#maybe add the training terminal commands themself to this? but then maybe need change path variables in code there