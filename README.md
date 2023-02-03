# Bruteforce Algorithm Generator

A simple script that generates all possible combinations of characters from a string of your choice. The script can generate combinations of a specified length range and will display the combinations in real-time, along with some additional information about the generation process.

__Please note that this script should not be used for malicious purposes. If used for such purposes, the user who ran the script will take full responsibility for any consequences.__

## Usage
To run the script, you will need to have Python installed on your computer. Follow these steps:

1. Clone the repository to your local machine.
2. Open a terminal window and navigate to the directory where you cloned the repository.
3. Run the following command: `python combination_generator.py`

You will then be prompted to enter the string of possible characters, followed by the range of characters in each combination. For example, if you want to generate combinations using the string "abcdefg!@#$%" and you want the combinations to range from 4 to 6 characters, you would enter the following:

```
BTF chars: abcdefg!@#$%
BTF length (start end): 4 6
out>
aaaa 4/6 20735 3255551
aaab 4/6 20734 3255550
..
aaa% 4/6 20724 3255540
aaba 4/6 20723 3255539
aabb 4/6 20722 3255538
aabc 4/6 20721 3255537
......
%%%% 4/6 0 3234816
aaaaa 5/6 248831 3234815
aaaab 5/6 248830 3234814
aaaac 5/6 248829 3234813
..............
...........
........
.....
..
```
The script will then begin generating the combinations and display them, along with some additional information, in real-time in the terminal window.

## Explanation

The script uses a simple algorithm to generate all possible combinations of characters from a string of your choice. It starts by generating combinations of the specified minimum length and then continues to generate combinations of increasing length until it reaches the specified maximum length. The combinations are displayed in real-time, along with the current length of the combinations being generated, the number of combinations left to be generated in the current length, and the number of combinations left to be generated until the generation of all combinations is complete.

### Project signed

KveKat x GPT-3.5
