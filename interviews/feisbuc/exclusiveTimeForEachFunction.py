""" 
- I was not able to copy and paste this so description is made from what I remember.
- Because of the above, the format might be different from what was presented in the interview
- I was not able to code a solution but was able to arrive to the correct algorythm

Problem starts here
You are given a list of instructions in the following format:

- first position: function name
- second position: arrival time
- third position: type of instruction. Only two types, begin (b) or end (e)

you need to return the sum of the exclusive time each function runned

Example:
    Input = [
        ["foo", 10, "b"],
        ["bar", 20, "b"],
        ["bar", 40, "e"],
        ["foo", 50, "e"]
    ]

    Output = {
        "foo": 20,
        "bar": 0
    }

    Explanation

        0   10   20   30   40   50   60
            foo................foo
                 bar......bar

        foo runned from time 10 to time 50
        bar runned from time 20 to 40
    
        foo runned exclusively from 10 to 20 and from 40 to 50
        bar never runned exclusively

        fo exclusive time = 20 - 10 + 50 - 40 = 20 
"""

"""
Proposed solution
Create the following strucutres and values: 
    - Dictionary that will serve as response
    - Dictionary that represent the current running functions and the time they started:
        - ex: {"foo": 10} 
    - currentTime integer to know current instruction time

Algorythm:
    - pop input list til its empty
    - change current time to the time of the instruction
    - if function is type b:
        - add it to the running functions dict.

    - if function is type e:
        - delete it from the running functions dict

    - if directory size is 1:
        - modify response dict by adding the time the function was alone
"""
from typing import List


def exclusiveTimeForEachFunction(input: List):
    response = dict()
    currentRunning = dict()
    currentTime = 0

    for functionName, _, _ in input:
        response[functionName] = 0

    while len(input):
        functionName, arrivalTime, type = input.pop(0)
        currentTime = arrivalTime

        if type == "b":
            if len(currentRunning) == 1:
                currentRunningFunctionName, currentRunningArrivalTime = list(
                    currentRunning.items()
                )[0]

                response[currentRunningFunctionName] += (
                    currentTime - currentRunningArrivalTime
                )

            currentRunning[functionName] = arrivalTime

        elif type == "e":
            del currentRunning[functionName]

            if len(currentRunning) == 1:
                currentRunningFunctionName = list(currentRunning.keys())[0]
                currentRunning[currentRunningFunctionName] = currentTime

        else:
            return {"error": "unknown type name"}

    return response


"""
    currentTime = 50

    response = {
        foo: 20 - 10 = 10
        bar: 0
    }

    currentRunning = {
        foo: 40
    }
"""

input = [["foo", 10, "b"], ["bar", 20, "b"], ["bar", 40, "e"], ["foo", 50, "e"]]

response = exclusiveTimeForEachFunction(input)
print("response", response)
