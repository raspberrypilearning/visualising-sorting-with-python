# Visualising Sorting with Python 1 - Graphing Data

This lesson will introduce students to visualising data by using Python's Matplotlib library.

In order for the students to follow this lesson, they will need to be using computers with Python3 and Matplotlib installed

To install Matplotlib, follow the instructions below

### Linux (Debian based distro)
1. Open up a terminal
2. `sudo apt-get install python3-matplotlib`

### Mac OS X and Windows
1. Either install with pip - `pip3 install matplotlib`
2. Or install from the matplotlib website - http://matplotlib.org/faq/installing_faq.html#how-to-install

## Learning objectives

- To understand how to use a simple list comprehension to create a random list of numbers
- To be able to produce simple graphs using matplotlib

## Learning outcomes

### All students are able to

- Use a list comprehension to produce a random list of numbers
- Plot a simple scatter graph using matplotlib

### Most students are able to

- Plot a variety of different graphs using matplotlib
- Plot an interactive graph using matplotlib

### Some students are able to

- Add axis and title to a matplotlib graph

## Lesson Summary

Learning about sorting algorithms is a particularly dry topic for many students. By allowing students to produce a variety of sorting algorithms , and visualise them running, they will gain a greater appreciation for what the algorithms are doing hopefully find the topic a little more interesting.

## Starter ##

- Ask students about the different ways we have of visualising data.
- Ask what might be the most appropriate graphs to visualise the following data sets:
1. The percentages of people who voted for different parties in an election.
2. The changes in a population of deer over the course of a decade.
3. The average temperatures each day over the course of a month.

## Main development

- Students should work through the first part of the worksheet, which introduces them to the concept of list comprehensions to construct lists of numbers.

- After the majority of students have complete the list comprehension exercises, you can have a quick competition to see who can write list comprehensions to create the following lists.

1. `[0,1,2,3,4,5,6,7,8,9]`
2. `[5,6,7,8,9]`
3. `[-9,-8,-7,-6,-5,-4,-3,-2,-1,0]`
4. `[0,2,4,6,8,10]`
5. `[[0,0,0],[1,1,1],[2,2,2]]`

The solutions are
1. `[i for i in range(10)]`
2. `[i for i in range(5,10)]`
3. `[i for i in range(-9,1)]`
4. `[i for i in range(0,11,2)]` or `[i for i in range(0,12,2)]`
5. `[[i] * 3 for i in range(3)]`

- Students should then work through the second part of the worksheet which introduces them to the concept of drawing graphs with matplotlib.

- After the majority of students have completed the graphing tasks, you can have a quick competition to see who can write code to create the following graphs.


## Plenary

Plenary...

## Homework

- Something
- Something else
