import os
import cv2
import sys

#most of the code here is for method 2, code for method 1 and 3 is below this.
def get_total_frames(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video - {video_path}")
        return None

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    cap.release()
    return total_frames

def extract_label_from_path(video_path):
    parent_folder = os.path.basename(os.path.dirname(video_path))
    return parent_folder

def create_annotation_file(data_dir, project_dir, annotation_file):
    with open(annotation_file, 'w') as f:
        for root, dirs, files in os.walk(data_dir):
            for video_file in files:
                if video_file.endswith('.MP4'):  # Add more video file extensions if needed
                    video_path = os.path.join(root, video_file)
                    total_frames = get_total_frames(video_path)
                    if total_frames is not None:
                        label = extract_label_from_path(video_path)
                        video_path = video_path.split(os.path.join(project_dir, ""))[-1] #add current computer path, -1 is end of sring array
                        f.write(f"{video_path} {total_frames} {label}\n")
#code for methods 1 and 3

def action_to_number(action_name):
    return action_numbers.get(action_name, -1)


def create_simple_annotation_file(data_dir, annotation_file):
    with open(annotation_file, 'w') as f:
        for root, dirs, files in os.walk(data_dir):
            for video_file in files:
                if video_file.endswith('.MP4'):  # Add more video file extensions if needed
                    video_path = os.path.join(root, video_file)
                    total_frames = get_total_frames(video_path)
                    if total_frames is not None:
                        label = extract_label_from_path(video_path)
                        video_path = video_path.split()[-1] #add current computer path, -1 is end of sring array
                        f.write(f"{video_path} {action_to_number(label)}\n")


project_path = os.getcwd()
project_directory = os.path.dirname(project_path)
data_directory = os.path.join(project_path, "mmaction2", "DataSet", "Data")
output_annotation_file = os.path.join(project_path, "mmaction2", "DataSet", "annotation.txt")
method = int(sys.argv[1])
if method == 2: #code for regular annotation file which will be delt with later on
    create_annotation_file(data_directory, project_directory, output_annotation_file)
else: #will create simple anno file using new function that is written bellow
    action_numbers = {
        "Close": 0,
        "Cutting": 1,
        "Electric_screwing_in": 2,
        "Electric_screwing_out": 3,
        "Hammering_in": 4,
        "Hammering_out": 5,
        "Measuring": 6,
        "Plug": 7,
        "Unplug": 8,
        "Screwing_in": 9,
        "Screwing_out": 10,
        "Tug_out": 11,
        "Tug_in": 12,
        "Turning_in": 13,
        "Turning_out": 14,
        "Open": 15,
        "Click": 16,
        "Piping": 17,
        "Cover": 18,
        "Uncover": 19,
        "Lift": 20,
        "Unlift": 21
    }
    create_simple_annotation_file(data_directory, output_annotation_file)
