import os
import subprocess


def compress_video(input_file, output_file, crf=23):
    """
    Compresses a video file using FFmpeg.

    Args:
        input_file (str): Path to the input video file.
        output_file (str): Path to save the compressed video file.
        crf (int): Constant Rate Factor (CRF) value for video quality (0-51, lower is better quality).
    """
    ffmpeg_cmd = f"ffmpeg -i {input_file} -c:v libx264 -crf {crf} {output_file}"
    subprocess.run(ffmpeg_cmd, shell=True)


def main(): #Change dir to methods if I put this in project
    project_path = os.getcwd() #maybe need dir name of that if this is not runed from filesToRun.py
    project_directory = os.path.dirname(project_path)
    data_directory = os.path.join(project_path, "mmaction2", "DataSet", "Data")
    output_annotation_file = os.path.join(project_path, "mmaction2", "DataSet", "annotation.txt")

    input_dir = os.path.join(project_path, "mmaction2", "DataSet", "Data")
    output_dir = os.path.join(project_path, "mmaction2", "DataSet")
    crf = 23  # Adjust the CRF value as needed for desired quality/size trade-off

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            if filename.endswith('.MP4'):
                input_path = os.path.join(root, filename)
                output_path = os.path.join(output_dir, os.path.relpath(input_path, input_dir))
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                try:
                    compress_video(input_path, output_path, crf=crf)
                    print(f"Compressed {input_path} saved to {output_path}")
                except Exception as e:
                    print(f"Error compressing {input_path}: {e}")


if __name__ == "__main__":
    main()
