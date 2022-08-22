Selected technology stack
- python 3
- selenium
- pytest

Reasons behind the chosen framework and pattern(s)
- the main reason would be that python is one of the easiest and most popular languages for test automation, 
it has all possible libraries for any automation purposes, and allows fast development time
- I have chosen pytest over other frameworks because it is easily customizable and have great support, and also
usually better than for example behave, because you don't need to add additional file just for steps
- for frontend I used pageobject patter, it usually the most understandable way to make UI tests, 
where you have every useful object for page in page class itself
- backend is quite similar but divided by functional rather than "pages"

How to run autotests
- install the last version of python3  https://www.python.org/downloads/
- install pip for the python https://pip.pypa.io/en/stable/installation/
- go to your project directory in console
- install requirements.txt from console via pip install -r requirements.txt"
- run with "pytest" in the main folder, pytest marks also supported, for example: "pytest -m backend"


Possible improvements
- add ability to configure test parameters via environment variables and config files
- remove login data from test and make a secure way to store a passwords for test users
- add ability to run test in different browsers and modes
- create a docker container for Jenkins
- add allure reporting for tests
- add screenshots on failure or even video recording of failed test runs
- make logger actually useful in tests
- add yapf and default style to make sure that format for all new features are same
- for a backend part, I would have added some kind of backend fixture on the top level with logger, curlyfy and
custom errors for different responses, this fixture would be usable for both frontend and backend tests
- also site and endpoint are hardcoded, they should be customizable, via env or configs
- and for backend I'm not handling headers in any way, it is pretty unusual, usually we need to add some fixture or 
method to at least generate and store token for API requests 
