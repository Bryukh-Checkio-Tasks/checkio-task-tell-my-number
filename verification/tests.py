"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [ (2,3), (3,5), (2,7) ],
            "answer": 23
        },
        {
            "input": [ (1,5), (4,7) ],
            "answer": 11            
        },
        {
            "input": [ (1,3), (2,5), (3,7) ],
            "answer": 52
        },
        {
            "input": [ (1,2), (1,3), (1,5) ],
            "answer": 1
        },
        {
            "input": [ (2,4), (7,9) ],
            "answer": 34
        },
        {
            "input": [ (2,11), (3,12), (4,13), (5,17), (6,19) ],
            "answer": 150999
        },
        {
            "input": [ (31, 49), (6,20) ],
            "answer": 766
        },
        {
            "input": [ (1,2), (2,5), (3,7), (4,9) ],
            "answer": 157
        },
        {
            "input": [ (1,7), (2,8), (3,9) ],
            "answer": 498
        },
        {
            "input": [ (3,4), (7,9), (22,25), (45,49) ],
            "answer": 29347
        },
        {
            "input": [ (3,4), (7,9), (22,25) ],
            "answer": 547
        },
        {
            "input": [ (1,2), (3,7), (5,15) ],
            "answer": 185
        },
        {
            "input": [ (1,19), (14,17), (1,12) ],
            "answer": 3193
        },
        {
            "input": [ (2,3), (3,5), (4,7), (5,11) ],
            "answer": 368
        }
    ],
    "Extra": [
        {
            "input": [ (2, 3), (3,4), (1,5) ],
            "answer": 11
        },
        {
            "input": [ (1, 2), (2,5), (6,7) ],
            "answer": 27
        },
        {
            "input": [ (3,4), (2,3), (4,5) ],
            "answer": 59
        },
        {
            "input": [ (4,5), (6,8), (8,9) ],
            "answer": 134
        },
        {
            "input": [ (1,2), (2,3), (3,5) ],
            "answer": 23
        },
        {
            "input": [ (0,2), (0,3), (1,5), (6,7) ],
            "answer": 6
        },
        {
            "input": [ (1,3), (6,7), (5,11) ],
            "answer": 181
        },
        {
            "input": [ (3,11), (2,12), (1,13) ],
            "answer": 14
        },
        {
            "input": [ (2,3), (3,5), (0,7) ],
            "answer": 98
        },
        {
            "input": [ (2,3), (3,5), (4,7) ],
            "answer": 53
        },
        {
            "input": [ (3,4), (4,5) ],
            "answer": 19
        }
        
        
    ]
}
