# Overview <br />

The program is designed for Insight Data Engineering Code Challenge, which is implemented in python mainly <br />

#Software requirement: <br />

Require python 2.7, collections, requests. <br />
The program is implemented in linux, need "split" and "wc" command. For windows user, please use cygwin <br />

#To run the code: <br />

use "run.sh" to run the code and use 'gen_input.sh' to generate fake tweet for testing if necessary. There will be three options <br />
[1] calculate feature 1 and 2 use single thread (for small amount of data,~500,000 lines of tweet) <br />
[2] calculate feature 1 and 2 using multi thread (recommended for large data) <br />
[3] clean all the data (if it says "rm: cannot remove '/*’: No such file or directory", you are still good. It means the file has been removed previously) <br />

#Design Idea: <br />

- **For storage** <br />
    use dictionary and list in python to store counted word and median, cPickle is used to store final results
- **For word count** <br />
    use collections.Counter for counting, split tweet by space. After parsing, merge two dictionary together
- **Find median** <br />
    use bisect.insort to sort the median array [o(nlog(n)) complexity] so that it can find median in o(1)
- **Implementation detail** <br />
    calculation, result storage and progress recording are done in feature_manager.py <br />
    It can resume unfinished work (every 500,000 lines by default) <br />
- **Test input** <br />
    "gen_test_input.py" is used to generate random strings for testing purpose <br />
- **Parallel computing** <br />
    to deal with large data, "multi_worker.py" do things in parallel.(6 thread by default) <br />
    for large file, split it into multiple small chunks for processing (15 small chunks by default) <br />
- **Customize setting** <br />
    please edit setting in "common_var.py" <br />

#IMPORTANT NOTE: <br />

- I assume previous tweets are not modified and every new tweet come in the end of "tweets.txt" <br />
- The code will record the number of tweet that has been parsed, neglected those have been parsed <br />
- It can not deal with modification of previous tweet, but this function can be added easily <br />
- **Please clear data before switching between single worker and multiple workers** <br />

#Some test results: <br />
The result is tested on a Lenovo W540 (i7, 8GB). The test inputs are random strings
| Number of lines        | Single worker           | Multiple worker (6 threads)  |
| ------------- |:-------------:| -----:|
| 200,000      | 8.5538s | 14.0397086s |
| 500,000      | 36s      |   26.7449s |
| 1,000,000 | 144.865358829s      |    91.3351509571s |

