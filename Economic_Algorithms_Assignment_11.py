import statistics
from typing import List


def compute_budget(total_budget:float,citizen_votes:List[List]) -> List[float]:
    n = len(citizen_votes)
    t = 1/n
    subjects = len(citizen_votes[0])
    # create a list of n-1 functions and calculate the value for each one of them according to t = 1/n
    Functions = [0] * (n-1)
    for i in range(1,n):
        Functions[i-1] = total_budget * min(1,i*t)
    # create a list of lists for the extra votes , the list should be :
    # [[total_budget * (1/n-1) , total_budget * (1/n-1) , total_budget * (1/n-1)] , [total_budget * (2/n-1) , total_budget * (2/n-1) , total_budget * (2/n-1)]...
    # [total_budget * (n-2/n-1) ,total_budget * (n-2/n-1) ,total_budget * (n-2/n-1)]]
    extra_votes = []
    for i in range(0,n-1):
        extra_votes.append([])
        for j in range(0,subjects):
            extra_votes[i].append(Functions[i])
    #unite the 2 lists , the original votes and the extra votes
    total_votes = citizen_votes+extra_votes
    #calculate the median for each subject
    answer = []
    for i in range(0,subjects):
        tmp = []
        for j in range(0,(2*n -1)):
            tmp.append(total_votes[j][i])
        tmp.sort()
        median = statistics.median(tmp)
        answer.append(median)
    return answer




