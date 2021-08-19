'''
    Problem Statement:

Write a python program which accepts student grade, number of backlogs as input 
and displays whether a student is eligible for a particular placement exam or not. 

Eligibility Criteria for a student to write placement exam:

Student should have minimum of 7 CGPA and maximum 2 backlogs.

Example 1:

Input:

6.5

2
Output:

Student is not eligible to write placement exam as he/she is not meeting the eligibility criteria.

Example 2:

Input:

7.0

4
Output:

Student is not eligible to write placement exam as he/she is not meeting the eligibility criteria.

Example 3:

Input:

8.0

0
Output:

Student is eligible to write placement exam.  
'''

def check_eligibility(grade, backlogs):
    if grade >= 7.0 and backlogs <= 2:
        print("Student is eligible to write placement exam.")
    else:
        print("Student is not eligible to write placement exam as he/she is not meeting the eligibility criteria.")

grade = float(input())
backlogs = int(input())
check_eligibility(grade, backlogs)