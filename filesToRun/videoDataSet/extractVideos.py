import os
import shutil
import time
import sys


def process_videos(data_dir, project_dir, annotation_files, output_dir, keep):
    # Delete existing train, val, test folders and create new ones
    for folder in ['train', 'val', 'test']:
        folder_path = os.path.join(output_dir, folder)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        os.makedirs(folder_path)
    for set_type, annotation_file in annotation_files.items():
        with open(annotation_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                video_path, label = line.strip().split()
                video_path = os.path.join(project_dir, video_path)
                output_subdir_path = os.path.join(output_dir, set_type)
                shutil.copy(video_path, output_subdir_path)
                if not keep:
                    os.remove(video_path)  # this and following for loop removes data for prevent disk quoda exceed
    if not keep:
        for root, dirs, files in os.walk(data_dir):
            for directory in dirs:
                dir_path = os.path.join(root, directory)
                shutil.rmtree(dir_path)


keepData = bool(int(sys.argv[1]) - 1)
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
process_videos(data_directory, project_directory, annotation_files, output_dir, keepData)

