__author__ = 'randxie'
import os, logging

# input folder and file
input_dir='tweet_input'
input_filename='tweets.txt'
in_file=os.path.join(os.getcwd(),input_dir,input_filename)

# output folder and file
output_dir='tweet_output'
feature1_txt_name='ft1.txt'
feature2_txt_name='ft2.txt'

# storage file for single worker
storage_dir='tmpvar'
storage_file='data_storage.p'
storage_filename=os.path.join(storage_dir,storage_file)

# storage file for multi-workers
storage_dir_txt=os.path.join(storage_dir,'multiworker_txt')
storage_dir_p=os.path.join(storage_dir,'multiworker_p')
head_file=os.path.join(storage_dir_txt,'head.txt')
tail_file=os.path.join(storage_dir_txt,'tail.txt')

# log file
log_file='logging.log'

# parameter for storage
s_para={}
s_para['storage_filename']=storage_filename         # define storage file

# parameter for calculating features
f_para={}
f_para['in_file']=in_file                           # define input files

# adjustable parameters
f_para['line_to_print']=100000                      # print progress every XXXX lines
f_para['line_to_save']=5*f_para['line_to_print']    # save intermediate calculation result every XXXX lines

# define tweet separator
separator=' '

# number of parallel computing worker
num_of_worker=6                                     # number of thread in multi-threading
num_of_split_file=15                                # split input file into 15 small files