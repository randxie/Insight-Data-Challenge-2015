__author__ = 'randxie'
# functions that support other modules
import logging, os
from common_var import log_file, output_dir, feature1_txt_name, feature2_txt_name, storage_dir_p, storage_dir_txt

# set up logging to file
def set_logging_config():

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=log_file,
                        filemode='w')

    # output logging info to screen as well (from python official website)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

# for finding median in a sorted array o(1)
def find_median(wordnum_list):
    if len(wordnum_list) % 2 ==0:
        idx=len(wordnum_list)/2
        return (wordnum_list[idx-1]+wordnum_list[idx])/2.0
    else:
        idx=(len(wordnum_list)+1)/2
        return wordnum_list[idx-1]

# get number of line in file
def get_file_line(in_file):
    num_lines=os.popen('wc -l %s'%(in_file)).read()
    return int(num_lines.split(' ')[0])

# write first feature to txt
def output_feature1(word_storage):
    logging.info ('start output features 1')
    out_file=os.path.join(os.getcwd(),output_dir,feature1_txt_name)
    with open(out_file, "w") as f:
        for key in sorted(word_storage):
            f.writelines('%s\t%d\n' %(key,word_storage[key]))

# write second feature to txt
def output_feature2(median_arr):
    logging.info ('start output features 2')
    out_file=os.path.join(os.getcwd(),output_dir,feature2_txt_name)
    with open(out_file,'w') as f:
        f.writelines("%s\n" % item for item in median_arr)

# clean temporary files
def clean_tmp_file():
    os.system('rm %s'%(os.path.join(os.getcwd(),storage_dir_txt,'*')))
    os.system('rm %s'%(os.path.join(os.getcwd(),storage_dir_p,'*')))