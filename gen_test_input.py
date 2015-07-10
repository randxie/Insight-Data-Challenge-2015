__author__ = 'randxie'
# function for generating random words as input for testing program
import requests, os, random, time

# define input folder and file name
input_dir='tweet_input'
input_filename='tweets.txt'
out_file=os.path.join(os.getcwd(),input_dir,input_filename)

# get english word list
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
words = response.content.splitlines()

# adjustable parameters
MaxWordSize=len(words)      # length of corpus
MaxTweetLength=50           # max word number contain in one tweet
MaxTweetNumber=1000000       # max number of tweet
ProgressLine=50000          # print out progress at multiple of certain line
start_time = time.time()    # get start time

# start generating fake input
with open(out_file,'w') as f:
    print('start generating fake tweet')
    for i in range(0,MaxTweetNumber):
        # print out progress
        if i%ProgressLine==0:
            print('finished %f%%' %(i*1.0/MaxTweetNumber*100))
        # random length of tweet
        tmp=random.randrange(1,MaxTweetLength)
        random_str=''
        # generate random strings
        for j in range(0,tmp):
            random_str=random_str+words[random.randrange(0,MaxWordSize-1)]+' '
        random_str=random_str+words[random.randrange(0,MaxWordSize-1)]
        f.writelines("%s\n" %random_str)
print('finished 100%%')

# print out used time
elapsed_time = time.time() - start_time
print('use time: %s second' %str(elapsed_time))
