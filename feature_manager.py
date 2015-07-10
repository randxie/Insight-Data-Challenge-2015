__author__ = 'randxie'
# Single thread feature generation class

import collections, os, bisect, logging, time
import cPickle as pickle # use cPickle to store intermediate variables
from common_var import output_dir, feature2_txt_name, feature1_txt_name, separator
from support_fun import find_median

# features are implemented use class
class feature_manager():
    def __init__(self,s_para):
        # read in parameters
        self.storage_filename=s_para['storage_filename']
        if 'worker_no' in s_para:
            self.worker_no=s_para['worker_no']
        else:
            self.worker_no='main worker'
        # initialize if there is no past input, else read in past data
        if not os.path.exists(self.storage_filename):
            # initialization
            self.word_storage={}            # store word and its number of appearance
            self.unsorted_indiv_word_arr=[] # an unsorted array storing how many individual word exists in each tweet
            self.indiv_word_arr=[]          # an sorted array storing how many individual word exists in each tweet
            self.last_word_pos=0            # define a line pointer to record which tweet it is pointing
            self.median_arr=[]              # for storing median
            self.is_save=False
        else:
            #read in past data
            with open(self.storage_filename,'rb') as f:
                data=pickle.load(f)
                self.unsorted_indiv_word_arr=data['self.unsorted_indiv_word_arr']
                self.word_storage=data['word_storage']
                self.indiv_word_arr=data['indiv_word_arr']
                self.median_arr=data['median_arr']
                self.last_word_pos=data['last_word_pos']
                self.is_save=True

    # input line for parsing and features calculation
    def input_word(self,line):
        word_list=line.split(separator)
        word_list[-1]=word_list[-1].strip('\n').strip(' ')
        word_counter=collections.Counter(word_list)
        # input median into array and sort them
        bisect.insort(self.indiv_word_arr,len(word_counter))
        self.unsorted_indiv_word_arr.append(len(word_counter))
        for key,value in word_counter.items():
            if key in self.word_storage:
                self.word_storage[key]=self.word_storage[key]+value
            else:
                self.word_storage[key]=value
        # store calculated median
        self.median_arr.append(find_median(self.indiv_word_arr))
        self.is_save=False
        self.last_word_pos=self.last_word_pos+1


    # main function (for calculating features)
    def calculate_feature(self,f_para):
        # read in parameters
        in_file=f_para['in_file']
        line_to_print=f_para['line_to_print']
        line_to_save=f_para['line_to_save']

        # see how many lines in the file
        self.add_logging('start estimating workload')
        num_lines=os.popen('wc -l %s'%(in_file)).read()
        num_lines=int(num_lines.split(' ')[0])
        self.add_logging('total tweet number is %d' %(num_lines))

        # open input file and start calculation
        with open(in_file,'r') as f:
            iter=0
            last_line=self.get_last_pos()
            self.add_logging('lastly loaded tweet is in line: %d' %(last_line+1))
            self.add_logging('starting at %f%%' %((last_line)*100.0/num_lines))
            self.add_logging('go to the tweet loaded last time')
            start_time = time.time()
            # parse tweet line by line
            for line in f:
                if iter>=last_line:
                    # input word into feature manager
                    self.input_word(line)
                    if (iter+1) % line_to_print ==0:
                        logging.info ('finished %f%%' %((iter+1)*100.0/num_lines))
                        # save at certain line for safety (modify "line_to_save" for controlling)
                        if (iter+1) % line_to_save ==0:
                            logging.info ('save up to line %d' %(iter+1))
                            self.save_feature()
                iter=iter+1
            self.save_feature()
            self.add_logging ('finished %f%%' %(100))
            elapsed_time = time.time() - start_time
            self.add_logging('feature calculation takes time: %s second' %str(elapsed_time))

    # return progress, when new tweets come in, no need to recalculate
    def get_last_pos(self):
        return self.last_word_pos

    # save temporary variable for feature calculation
    def save_feature(self):
        if not self.is_save:
            tmpdict={'word_storage':self.word_storage,'indiv_word_arr':self.indiv_word_arr,\
                    'median_arr':self.median_arr,'last_word_pos':self.last_word_pos,\
                    'self.unsorted_indiv_word_arr':self.unsorted_indiv_word_arr}
            pickle.dump(tmpdict,open(os.path.join(os.getcwd(),self.storage_filename),'wb'))
        self.is_save=True
        self.add_logging('finish saving')

    def add_logging(self,str):
        logging.info(self.worker_no+': '+str)

    # delete tmp file and output files
    def __delete_all__(self):
        logging.warning ('Deleted all data')
        os.system("rm "+os.path.join(os.getcwd(),self.storage_filename)+' '+\
                  os.path.join(os.getcwd(),output_dir,feature2_txt_name)+' '+\
                  os.path.join(os.getcwd(),output_dir,feature1_txt_name))


