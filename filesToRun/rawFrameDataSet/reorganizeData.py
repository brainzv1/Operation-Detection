import os
import sys

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

#Counts number of raw frames after chosen % to keep
def count_jpg_files(folder_path):
    jpg_files = [file for file in os.listdir(folder_path) if file.endswith('.jpg')]
    return len(jpg_files)


# Define the paths for train, test, and val directories
project_path = os.getcwd()
train_dir = os.path.join(project_path, "mmaction2/DataSet/train/")
test_dir = os.path.join(project_path, "mmaction2/DataSet/test/")
val_dir = os.path.join(project_path, "mmaction2/DataSet/val/")

data_directory = os.path.join(project_path, "mmaction2", "DataSet", "Data")
output_annotation_file = os.path.join(project_path, "mmaction2", "DataSet", "annotation.txt")
output_train_file = os.path.join(project_path, "mmaction2", "DataSet", "train.txt")
output_val_file = os.path.join(project_path, "mmaction2", "DataSet", "val.txt")
output_test_file = os.path.join(project_path, "mmaction2", "DataSet", "test.txt")

# Function to convert action names to numbers - it is necessary for running train
def action_to_number(action_name):
    return action_numbers.get(action_name, -1)  # Returns -1 if action_name is not found

# Read the original train file content
with open(output_train_file, 'r') as train_file:
    train_lines = train_file.readlines()

# Open the train file for writing to overwrite it with the modified format
with open(output_train_file, 'w') as train_file:
    for line in train_lines:
        video_path, *additional_info = line.strip().split()
        video_name = os.path.splitext(os.path.basename(video_path))[0]
        frames_count = count_jpg_files(os.path.join(train_dir, video_name))
        action_name = additional_info[-1]  # Converts to number, action name is the last element in additional_info
        action_number = action_to_number(action_name)
        if action_number == -1:
            print(f"Unknown action name: {action_name}")
            continue

        additional_info[-1] = str(action_number) # Replace the original action name with its number
        additional_info[-2] = str(frames_count)  # Replace the original frame count with the count of JPG files copied
        output_line = os.path.join(train_dir, video_name) + ' ' + ' '.join(additional_info) + '\n'
        train_file.write(output_line)

# Same for val and test files
with open(output_val_file, 'r') as val_file:
    val_lines = val_file.readlines()

with open(output_val_file, 'w') as val_file:
    for line in val_lines:
        video_path, *additional_info = line.strip().split()
        video_name = os.path.splitext(os.path.basename(video_path))[0]
        frames_count = count_jpg_files(os.path.join(val_dir, video_name))
        action_name = additional_info[-1]  # Converts to number, action name is the last element in additional_info
        action_number = action_to_number(action_name)
        if action_number == -1:
            print(f"Unknown action name: {action_name}")
            continue

        additional_info[-1] = str(action_number)  # Replace the original action name with its number
        additional_info[-2] = str(frames_count)  # Replace the original frame count with the count of JPG files copied
        output_line = os.path.join(val_dir, video_name) + ' ' + ' '.join(additional_info) + '\n'
        val_file.write(output_line)

with open(output_test_file, 'r') as test_file:
    test_lines = test_file.readlines()

with open(output_test_file, 'w') as test_file:
    for line in test_lines:
        video_path, *additional_info = line.strip().split()
        video_name = os.path.splitext(os.path.basename(video_path))[0]
        frames_count = count_jpg_files(os.path.join(test_dir, video_name))
        action_name = additional_info[-1]  # Converts to number, action name is the last element in additional_info
        action_number = action_to_number(action_name)
        if action_number == -1:
            print(f"Unknown action name: {action_name}")
            continue

        additional_info[-1] = str(action_number)  # Replace the original action name with its number
        additional_info[-2] = str(frames_count)  # Replace the original frame count with the count of JPG files copied
        output_line = os.path.join(test_dir, video_name) + ' ' + ' '.join(additional_info) + '\n'
        test_file.write(output_line)

