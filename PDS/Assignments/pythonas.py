"""
@author: DM

"""
import matplotlib.pyplot as plt
import numpy as np


survey_file = open ("survey_anon.txt","r")

#1
lines = 0
unix_score= 0

unix_count=[0,0,0,0,0]
db_count=[0,0,0,0,0]
prog_count=[0,0,0,0,0]

for line in survey_file:

	lines = lines + 1
	columns = line.strip().split("\t")
	
#Unix
 
 #I dont even understand the question
 #I have no experience working in a terminal
 #I have issued a few commands in a terminal based on given instructions
 #I have written simple terminal commands or done some system work on the term
 #I am a Unix hacker
 
	if columns[1] == "I dont even understand the question":
		unix_count[0] = unix_count[0] + 1
	elif columns[1] == "I have no experience working in a terminal":
		unix_count[1] = unix_count[1] + 1
	elif columns[1] == "I have issued a few commands in a terminal based on given instructions":
		unix_count[2] = unix_count[2] + 1
	elif columns[1] == "I have written simple terminal commands or done some system work on the terminal":
		unix_count[3] = unix_count[3] + 1
	elif columns[1] == "I am a Unix hacker":
		unix_count[4] = unix_count[4] + 1

#	print unix_count


# Database

#I am a database hacker
#I can write very complex queries when needed
#I can write simple queries and issue them to a database
#I have issued simple queries to a relational database based on given instructions
#I have never directly accessed a database

	if columns[2] == "I have never directly accessed a database":
		db_count[0] = db_count[0] + 1
	elif columns[2] == "I have issued simple queries to a relational database based on given instructions":
		db_count[1] = db_count[1] + 1
	elif columns[2] == "I can write simple queries and issue them to a database":
		db_count[2] = db_count[2] + 1
	elif columns[2] == "I can write very complex queries when needed":
		db_count[3] = db_count[3] + 1
	elif columns[2] == "I am a database hacker":
		db_count[4] = db_count[4] + 1


# programming

#I am a hacker or have  senior-level programming experience
#I can write complex programs, am familiar with programming design patterns, software testing, system design, and algorithms
#I can write simple programs to accomplish tasks I encounter
#I have written simple programs, based on instructions or a tutorial
#I have never programmed before.

	if columns[3] == "I have never programmed before.":
		prog_count[0] = prog_count[0] + 1
	elif columns[3] == "\"I have written simple programs, based on instructions or a tutorial\"":
		prog_count[1] = prog_count[1] + 1
	elif columns[3] == "I can write simple programs to accomplish tasks I encounter":
		prog_count[2] = prog_count[2] + 1
	elif columns[3] == "\"I can write complex programs, am familiar with programming design patterns, software testing, system design, and algorithms.\"":
		prog_count[3] = prog_count[3] + 1
	elif columns[3] == "I am a hacker or have  senior-level programming experience":
		prog_count[4] = prog_count[4] + 1
	

#Compute the average score 

unix_score = ((unix_count[0]*1)+(unix_count[1]*2)+(unix_count[2]*3)+(unix_count[3]*4)+(unix_count[4]*5))/float(lines)
db_score = ((db_count[0]*1)+(db_count[1]*2)+(db_count[2]*3)+(db_count[3]*4)+(db_count[4]*5))/float(lines)
prog_score = ((prog_count[0]*1)+(prog_count[1]*2)+(prog_count[2]*3)+(prog_count[3]*4)+(prog_count[4]*5))/float(lines)

# print count for each level per discipline
print unix_count
print db_count
print prog_count

#Print average score for each discipline
print unix_score
print db_score
print prog_score
all_class=dict(unix=unix_score,database=db_score,progamming=prog_score)
class_max=max(all_class,key=all_class.get)
class_min=min(all_class,key=all_class.get)
print "The highest overall skill level is in %s " %class_max
print "The lowest overall skill level is in %s " %class_min


 
#2.UNIX
#list of the # of each answer
#unix_vals = [unix1_count, unix2_count, unix3_count, unix4_count, unix5_count] 
unix_xval = [1, 2, 3, 4, 5]
#to substitute the strings describing the skill level with a numeric value
#starting from the lowest and going to the highest

plt.plot(unix_xval,unix_count)
plt.show()

#2.Database

db_xval = [1, 2, 3, 4, 5]

plt.plot(db_xval, db_count)
plt.show()

#2.Programming

prog_xval = [1, 2, 3, 4, 5]

plt.plot(prog_xval, prog_count)
plt.show()

#3.Combine these three plots, overlaying them on a single graph 
plt.plot(unix_xval,unix_count,db_xval,db_count,prog_xval,prog_count )

#Make sure each line is a different color for each line, 
plt.rc('axes', color_cycle=['r', 'g', 'b'])

#make a legend to tell the different colors apart.   
plt.legend(['Unix', 'Database', 'Programming'])
plt.show()

#4.bar plot

offset = 0.3
plt.bar(unix_xval,unix_count , offset, color='r',align='edge')
plt.bar(db_xval,db_count , offset, color='g',align='center')
plt.bar(prog_xval,prog_count , -offset, color='b',align='edge')

plt.title('Technical Skills')
plt.xlabel('Response')
plt.ylabel('No. Of Resonses')
plt.legend(['Unix', 'Database','Programming'])

#DIY Data Utilities
#1.There are many times where a data scientist gets some columnar data and wants to simply plot it. 
#take single column of numerical data from the command line via a unix pipe display that data in a plot. 
#Hint: use the stdin function in the sys module. Hint 2: you can run a python file from the unix terminal by typing:  python [your_py_file].py  
#2.Make a script similar that used in question 5 that makes a histogram instead of a line plot.
#3.(bonus) Extend the first plotting question so that the script can read multiple columns of input data instead of just 1.
#Plot them together in the same plot window.

#Income Prediction

