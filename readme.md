# Python challenge
Given a string, "compress" the string by replacing repeated characters with a character and a number.

The input string is limited to a-z and A-Z.

Examples:
aaabbbccc => a3b3c3 
  
  
# Solution
## Set up the environment
To execute the functionality you should clone the repo:
```
git clone https://www.github.com
```

Go into the new created folder and create a virtual environment:
```
cd tech-challenge
python3 -m venv venv
```

Activate the virtual environment:
```
source venv/bin/activate
```

Install the requirements:
```
pip3 install requirements.txt
```

## Try the code
Execute the code:
```
python3 -m main
```

## Run the tests
Execute:
```
python3 -m pytest -rA
```

## Find test coverage
Run:
```
coverage run -m pytest -rA
coverage report
```
