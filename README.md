# Prime solution



        Output:
        A list of all prime numbers which are smaller than the input-number.
        E.g.
          If input is 5
            Output is: 2, 3
          If input is 6
            Output is: 2, 3, 5



This script returns primes LESS than the starting number.
##Installation or requirements
Install the requirements before running
`pip install -r requirements.txt`

## Run script
`python -m prime_finder`

##Tests
To test run:
`python -m pytest prime_finder_tests.py`

###notes

- I have used type annotations to ensure the input is an int.
- I have added error handling.
- Requirements.txt file was built using `pip-compile requirements.in`
