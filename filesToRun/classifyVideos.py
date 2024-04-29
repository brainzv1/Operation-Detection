import os
import subprocess
import shutil

# Dictionary mapping category names to action numbers
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
# Function to convert action numbers to category names
def number_to_action(num):
    for key, value in action_numbers.items():
        if value == int(num):
            return key
    return None

# Function to create folders for each category
def create_category_folders():
    demo_folder = os.path.join(os.getcwd(), "demo")
    if not os.path.exists(demo_folder):
        os.makedirs(demo_folder)
    else:
        shutil.rmtree(demo_folder)
        os.makedirs(demo_folder)

    for category in action_numbers.keys():
        folder_path = os.path.join(demo_folder, category)
        os.makedirs(folder_path)

# Function to run demo.py for each video file
def run_demo_for_videos(test_folder, test_file):
    demo_folder = os.path.join(os.getcwd(), "demo")
    with open(test_file, 'r') as f:
        for line in f:
            video_path, category = line.strip().split()
            category = number_to_action(int(category))
            category_folder = os.path.join(demo_folder, str(category))
            model_path = os.path.join("work_dirs", "GoodEpochs", "best_acc_top1_epoch_30.pth")
            label_path = os.path.join("mmaction2", "demo", "label.txt")
            out_filename = f"predicted_results_{category}_{os.path.splitext(os.path.basename(video_path))[0]}.mp4"
            out_filepath = os.path.join(category_folder, out_filename)
            current_path = os.getcwd()
            # Check if output file already exists in category folder or its subfolders
            if os.path.exists(out_filepath):
                print(f"Skipping {video_path} - Output file already exists")
            else:
                # Run subprocess only if output file doesn't exist
                command = f"python mmaction2/demo/demo.py filesToRun/videoDataSet/videoDataSetTSNFile.py {model_path} {video_path} {label_path} --out-filename {out_filepath}"
                subprocess.call(command, shell=True)

def main():
    current_path = os.getcwd()
    test_folder = os.path.join(current_path, "mmaction2", "DataSet", "test")
    test_file = os.path.join(current_path, "mmaction2", "DataSet", "test.txt")
    create_category_folders() #if you want to get rid of existing data first
    run_demo_for_videos(test_folder, test_file)

if __name__ == "__main__":
    main()
