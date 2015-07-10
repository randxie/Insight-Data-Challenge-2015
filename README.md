The program is designed for Insight Data Engineering Code Challenge.

Software requirement:
    Require python 2.7, collections, requests.
    Code is implemented in linux, need "split" command. For windows user, please use cygwin

To run the code:
    use "run.sh" to run the code and you can use 'gen_input.sh' to generate fake tweet for testing. There will be three options
    [1] for calculating feature 1 and 2 use single thread
    [2] for calculating feature 1 and 2 using multi thread(recommended for large data)
    [3] for cleaning all the data

Design Idea:
    (1) First try MySQL to store calculated result (db_manager.py), but it is slow
    (2) Later, I decide to use cPickle directly to store features
    (3) Put all the calculation inside feature_manager.py
    (4) "gen_test_input.py" is used to generate random strings for testing purpose
    (5) "multi_worker.py" is used to calculate features in parallel
    (6) Please clear data before switching between option 1(single worker) and option 2(multiple worker)
    (7) Edit setting in "common_var.py"	

IMPORTANT NOTE:
    (1) I assume previous tweets are not modified and every new tweet come in the end of "tweets.txt"
    (2) The code will record the number of tweet that has been parsed, neglected those have been parsed
    (3) It can not deal with modification of previous tweet, but this function can be added easily

About output:
    feature 1: use "\t" to separate word and number of appearance

Some test results:
200000: single: 8.5538s multiple: 14.0397086s
500000: single:36s  multiple: 26.7449s
1000000: single: 144.865358829s multiple: 91.3351509571s

