The program is designed for Insight Data Engineering Code Challenge. <br />

Software requirement: <br />
    Require python 2.7, collections, requests. <br />
    Code is implemented in linux, need "split" command. For windows user, please use cygwin <br />

To run the code: <br />
    use "run.sh" to run the code and you can use 'gen_input.sh' to generate fake tweet for testing. There will be three options <br />
    [1] for calculating feature 1 and 2 use single thread(for small amount of data, ~500000) <br />
    [2] for calculating feature 1 and 2 using multi thread(recommended for large data) <br />
    [3] for cleaning all the data (if it says "file can not be remove due to not existing", you are still good. It means the file has been removed previously) <br />

Design Idea: <br />
    (1) First try MySQL to store calculated result (db_manager.py), but it is slow <br />
    (2) Later, I decide to use cPickle directly to store features <br />
    (3) Put all the calculation inside feature_manager.py <br />
    (4) "gen_test_input.py" is used to generate random strings for testing purpose <br />
    (5) "multi_worker.py" is used to calculate features in parallel <br />
    (6) Please clear data before switching between option 1(single worker) and option 2(multiple worker) <br />
    (7) Edit setting in "common_var.py"	

IMPORTANT NOTE: <br />
    (1) I assume previous tweets are not modified and every new tweet come in the end of "tweets.txt" <br />
    (2) The code will record the number of tweet that has been parsed, neglected those have been parsed <br />
    (3) It can not deal with modification of previous tweet, but this function can be added easily <br />

Some test results: <br />
(1) 200000: single: 8.5538s multiple: 14.0397086s; <br />
(2) 500000: single:36s  multiple: 26.7449s; <br />
(3) 1000000: single: 144.865358829s multiple: 91.3351509571s; <br />

