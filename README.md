# Locate Numbers

Welcome to the locate-numbersreadme, if you're reading this you're probably interested in working as a developer at PerfectPitchTech. We're excited to meet you, but first we have fun coding challenge for you to complete.

## Rules

  - **DO NOT** make a pull request back to this repository with your solution (otherwise other people can see your solution).
  - Your solution needs to be written in Python. Feel free to use any Python libraries or frameworks you feel are appropriate. (Docker solutions will have bound points!)

## Requirements

We have two tasks for you, 
1. Write an API that get the location of each number from a CSV file using [Libphone numbers library](https://pypi.org/project/phonenumbers/). We provide the numbers.csv in this repo, please generate and output.csv and include it in your solution.
2. Write an API that get a closest phone number based on another phone number 

After that please write a simple markdown file with some ideas about how you can improve the process time since the libphone library is quite slow. 

### Example Input 

````csv
numbers
(635) 474-8673
(489) 690-3885
(213) 416-0509
...
````

### Example Output
````csv
numbers, valid, location
(635) 474-8673, false, n/a
(489) 690-3885, false, n/a
(213) 416-0509, false, Los Angeles, CA
...
````

### Task 1 Example cURL command

````shell
curl -i -X POST -H "Content-Type: multipart/form-data" -F "numbers=@numbers.csv" http://localhost:9000/locate_numbers
````

### Task 2 Example cURL command

````shell
curl http://localhost:9000/locate_numbers?number=+13101231234
````
Result could be (213) 416-0509, since (310) 123 1234 and (213) 416-0509 are a Los Angeles phone number.

## Finished?

Please send your code, the markdown with the improvements and the output csv in a git repository to your contact at PerfectPitchTech and we'll be in touch with your from there. Thanks and happy coding.