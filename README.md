# TBP
The Traveling Beersman Problem is a problem posed by a friend of mine who wanted to find out the shortest path between pubs during a pub crawl with changing starting points.

This is a simple script for solving this problem.

## The input
Running the script, user is prompted to insert mor than one unique pub name. It's between these the TBP emerges.

There needs to be a file containing all the pubs questioned.

This is named **pubs.txt**

This file is loaded for all TBP problems and is laid out like so:

    me,pub1,distance
    me,pub2,distance
    pub1,pub2,distance

where *me* is the distance between your position and *pub1*, *pub1* and *pub2* are pub names and *distance* is the distance between them, preferably an integer.

## The output
It's really the first, shortest match that is printed.

## Notes
If you are about to enter more than 11 pubs, you have to wait *a little* since this is a brute force solution... 

(My laptop ran 11 pubs in around 5 minutes...)
