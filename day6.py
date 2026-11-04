#Day6: Debugging tracebacks, logging, reproducible bug reports, Git and Code review basics.

#1. Debugging tracebacks: Tracebacks are error messages that provide information about the sequence of function calls that led to an error in a program.
#  They help developers identify the source of the error and understand the context in which it occurred.
#  When a program encounters an error, it generates a traceback that includes the file name, line number, and function name where the error occurred, along with a description of the error itself.

def calculate_total():
    price = 100
    quantity = 5

    total = price * quntity

    return total


print(calculate_total())

#Output:   Traceback (most recent call last):
 # File "main.py", line 9, in <module>
  #  print(calculate_total())
  #File "main.py", line 5, in calculate_total
   # total = price * quntity
#NameError: name 'quntity' is not defined


#Python build-in debugger:pdb 
def calculate_total(price, quantity):

    total = price * quantity

    return total


breakpoint()  #breakpoint() is a built-in function in Python that allows you to pause the execution of your code at a specific point and enter an interactive debugging session.

result = calculate_total(100, 5)

print(result)

#2. Logging: Logging is the process of recording information about a program's execution, including errors, warnings, and other relevant events.
#  It helps developers monitor the behavior of their programs, diagnose issues, and track down bugs.
#  Logging can be done using various logging libraries or frameworks that provide different levels of logging (e.g., debug, info, warning, error) and allow developers to customize the output format and destination of log messages.     
import logging

import git

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logging.debug("Debugging information")
logging.info("Application started")
logging.warning("Low balance")
logging.error("Something went wrong")
logging.critical("Application failure")


#3. Reproducible bug reports: A reproducible bug report is a detailed description of a software bug that allows developers to consistently reproduce the issue.
#  It typically includes information about the environment in which the bug occurs, the steps to reproduce the bug, the expected behavior, and the actual behavior observed.
#  Reproducible bug reports are essential for effective debugging and help developers understand and fix issues more efficiently.    


#4. Git: Git is a distributed version control system that allows developers to track changes in their codebase, collaborate with others, and manage different versions of their software projects.
#  It provides features such as branching, merging, and commit history, enabling developers to work on multiple features or bug fixes simultaneously without interfering with each other's work.
#  Git also allows for easy collaboration through platforms like GitHub and GitLab, where developers can share their code, review changes, and contribute to open-source projects.
#Git Commands:
#git init: Initializes a new Git repository in the current directory.
#git clone: Creates a local copy of a remote Git repository.
#git add: Stages changes for the next commit.
#git commit: Records changes to the repository.
#git push: Uploads local commits to a remote repository.
#git pull: Downloads and merges changes from a remote repository.

#git init
#git add .
#git commit -m "Initial commit"
#git switch -c feature-logging
#git add .
#git commit -m "Add logging"


#git status
#make  the new file
#git branch <name of branch>
#switch to the new branch    git checkout <name of branch>
#git status
#git add .
#git commit -m "Add new feature"
#push it on the new branch   git push -u origin <name of branch>   Here -u is used for first time so it remember the branch name and next time we can use git push only.
#now go to the main branch
#then  merge the new branch to the main     git merge <name of new branch>
# to delete the branch after merging   git branch -d <name of new branch>



#.gitignore: A .gitignore file is a text file that specifies which files and directories should be ignored by Git when tracking changes in a repository.


#5. Code review basics: Code review is the process of examining and providing feedback on code written by other developers.
#  It helps ensure code quality, maintainability, and adherence to coding standards.
#  During a code review, reviewers check for issues such as bugs, performance problems, security vulnerabilities, and readability.
#  They may also suggest improvements or alternative approaches to solving a problem.
#  Code reviews can be conducted through various tools and platforms that facilitate collaboration and communication among team members.
