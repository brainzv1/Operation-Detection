import os
import cv2
import shutil
import random
import time
import sys


def extract_frames(video_path, output_dir, skip, timeout):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video - {video_path}")
        return
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    success, frame = cap.read()
    if success:
        count = 1
        start_time = time.time()  # read first frame so no folder is empty

        # Always copy the first frame
        frame_path = os.path.join(output_dir, f"img_{'{:05d}'.format(count)}.jpg")
        cv2.imwrite(frame_path, frame)
        count += 1
        while success:
            if time.time() - start_time > timeout:
                print(f"Skipping video {video_path} due to timeout.")
                break
            if random.random() <= skip or count == 1:  # Always copy the first frame
                frame_path = os.path.join(output_dir, f"img_{'{:05d}'.format(count)}.jpg")
                cv2.imwrite(frame_path, frame)
                count += 1

            success, frame = cap.read()

    #remove count+1 from if and add here if you need for at least 100% to work

    cap.release()


def process_videos(data_dir, project_dir, annotation_files, output_dir, skip, timeout, keep):
    # Delete existing train, val, test folders and create new ones
    for folder in ['train', 'val', 'test']:
        folder_path = os.path.join(output_dir, folder)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        os.makedirs(folder_path)

    # Process videos for train, val, and test sets
    for set_type, annotation_file in annotation_files.items():
        with open(annotation_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                video_path, total_frames_str, label = line.strip().split()
                total_frames = int(total_frames_str)
                video_path = os.path.join(project_dir, video_path)
                video_name = os.path.splitext(os.path.basename(video_path))[0]  # Extract video name without extension

                output_subdir_path = os.path.join(output_dir, set_type, video_name)
                os.makedirs(output_subdir_path, exist_ok=True)

                # Copy video file to appropriate folder
                #shutil.copy(video_path, output_subdir_path)

                # Extract frames
                extract_frames(video_path, output_subdir_path, skip, timeout)
                if not keep:
                    os.remove(video_path) #this and following for loop removes data for prevent disk quoda exceed
    if not keep:
        for root, dirs, files in os.walk(data_dir):
            for directory in dirs:
                dir_path = os.path.join(root, directory)
                shutil.rmtree(dir_path)


# Function to get all video files from a directory
#def get_video_files(directory):
#    video_file_list = []
#    for root, dirs, files in os.walk(directory):
#        for file in files:
#            if file.endswith('.mp4') or file.endswith('.avi'):
#                video_file_list.append(os.path.join(root, file))
#    return video_file_list


project_path = os.getcwd()
project_directory = os.path.dirname(project_path)

data_directory = os.path.join(project_path, "mmaction2", "DataSet", "Data")
output_annotation_file = os.path.join(project_path, "mmaction2", "DataSet", "annotation.txt")
output_train_file = os.path.join(project_path, "mmaction2", "DataSet", "train.txt")
output_val_file = os.path.join(project_path, "mmaction2", "DataSet", "val.txt")
output_test_file = os.path.join(project_path, "mmaction2", "DataSet", "test.txt")

annotation_files = {
    'train': output_train_file,
    'val': output_val_file,
    'test': output_test_file
}
output_dir = os.path.join(project_path, "mmaction2", "DataSet")
# Get all video files from the data directory
#video_files = get_video_files(data_directory)
#Note: The following code moved to filesToRun.py for better practice
#while True:
#    try:
#        user_input = int(input("What % of all frames do you want to keep?"))
#        if 0 < user_input <= 100:
#            skip_probability = 0.01 * user_input
#            break
#        else:
#            print("Please enter a value between 1 and 100.")
#    except ValueError:
#        print("Please enter a valid integer.")
timeout_duration = 60
# Process videos using the annotation files
skip_probability = float(sys.argv[1])
keepData = bool(int(sys.argv[2]) - 1)  # True is keep data and False is delete it

process_videos(data_directory, project_directory, annotation_files, output_dir, skip_probability, timeout_duration, keepData)







