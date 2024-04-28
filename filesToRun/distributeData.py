
#take all anno file text and mix it (all the lines randomly)
#create 3 new txt files, 70% train 20% valid 10% test train.txt val.txt  test.txt


import random
import os
import sys

project_path = os.getcwd()
output_annotation_file = os.path.join(project_path, "mmaction2", "DataSet", "annotation.txt")
output_train_file = os.path.join(project_path, "mmaction2", "DataSet", "train.txt")
output_val_file = os.path.join(project_path, "mmaction2", "DataSet", "val.txt")
output_test_file = os.path.join(project_path, "mmaction2", "DataSet", "test.txt")

with open(output_annotation_file, 'r') as anno:
   lines = anno.readlines()  # Read all lines from the ano file


# Shuffle the lines randomly
random.shuffle(lines)


# Calculate the number of lines for each set
total_lines = len(lines)
test_lines = int(total_lines * 0.1)
val_lines = int(total_lines * 0.2)
train_lines = total_lines - test_lines - val_lines


# Open train, val, and test files for writing
with open(output_train_file, 'w') as train_file, \
       open(output_val_file, 'w') as val_file, \
       open(output_test_file, 'w') as test_file:
   # Write lines to each file based on the calculated number of lines
   for i, line in enumerate(lines):
       if i < test_lines:
           test_file.write(line)
       elif i < test_lines + val_lines:
           val_file.write(line)
       else:
           train_file.write(line)
