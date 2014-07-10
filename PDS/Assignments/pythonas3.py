# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 23:56:05 2014

@author: DM
"""

print "-------------------------------------------------------"
print "Question - Education"
print "-------------------------------------------------------"


import matplotlib.pyplot as plt
import numpy as np
#import scikit-learn
marketdata = open ("marketing.data","r")
actual_income_list = []
predicted_income_list_ed = []
difference_list_ed = []
total_actual_income=0
total_predicted_income=0
# using genfrom txt - a more robust version of loadtxt
#DataIn=np.genfromtxt("marketing.data",missing_values=('NA'))
#print DataIn

ed_modifier_dict={1:-3,2:-1,3:0,4:1,5:3,6:4}
person_count=0
for line in  marketdata:
    t=line.strip().split(" ")
    # remove NA and blank columns
    if (len(t)<5) or (t[0]=="NA") or (t[4]=="NA") or (t[5]=="NA"):
        continue
    
    actual_income=int(t[0])
    actual_income_list.append(actual_income)
 
    predicted_income=4+ed_modifier_dict[int(t[4])]
    predicted_income_list_ed.append(predicted_income)
    difference=abs(float(predicted_income)-float(actual_income))
    difference_list_ed.append(difference)
    
    
    # count the number of instances
    person_count=person_count+1

#calculate totqal actual income
total_actual_income=sum(actual_income_list)
total_predicted_income=sum(predicted_income_list_ed)
avg_difference_ed=np.average(difference_list_ed)



print  "Total Instance: %0.0f " %person_count
print "Total Income_Actual (Level): %0.0f " %total_actual_income
print "Total Income_Predicted (Level): %0.0f " %total_predicted_income
print "Total difference is %0.0f " %sum(difference_list_ed)
print "Average difference per user is %f " %avg_difference_ed 

#2 Using both education level and occupation level
print "-------------------------------------------------------"
print "Question - Education + Occupation"
print "-------------------------------------------------------"


import matplotlib.pyplot as plt
import numpy as np
#import scikit-learn
marketdata = open ("marketing.data","r")
actual_income_list = []
predicted_income_list_ed_oc = []
abs_difference_list_ed_oc = []
difference_list_ed_oc = []
total_actual_income=0
total_predicted_income=0
person_count=0
exact_count = 0
over_count = 0
under_count = 0
oc_modifier_dict={1:2.5,2:-0.6,3:0,4:0.2,5:-0.5,6:-1.5,7:0.3,8:0.8,9:-2.5}
ed_modifier_dict={1:-3,2:-1,3:0,4:1,5:3,6:4}



for line in  marketdata:
    t=line.strip().split(" ")
    if (len(t)<5) or (t[0]=="NA") or (t[4]=="NA") or (t[5]=="NA"):
        continue
    
    actual_income=int(t[0])
    actual_income_list.append(actual_income)
 
    predicted_income_ed_oc=4+ed_modifier_dict[int(t[4])] + oc_modifier_dict[int((t[5]))]
    predicted_income_list_ed_oc.append(predicted_income_ed_oc)
    
    abs_difference=abs(float(predicted_income_ed_oc)-float(actual_income))
    abs_difference_list_ed_oc.append(abs_difference)
    
    difference=float(predicted_income_ed_oc)-float(actual_income)
    difference_list_ed_oc.append(difference)
    
    if float(predicted_income_ed_oc) == float(actual_income):
        exact_count =exact_count+1
    elif float(predicted_income_ed_oc) > float(actual_income):
        over_count =over_count+1
    else:
        under_count =under_count+1

    # count the number of instances
    person_count=person_count+1

#calculate totqal actual income
total_actual_income=sum(actual_income_list)
total_predicted_income=sum(predicted_income_list_ed_oc)
#total absolute difference 
total_abs_difference=sum(abs_difference_list_ed_oc)
#total difference 
total_difference=sum(difference_list_ed_oc)
#average of absolute difference
avg_abs_difference_ed_oc=np.average(abs_difference_list_ed_oc)
# average of difference
avg_difference_ed_oc=np.average(difference_list_ed_oc)

print  "Total Instance: %0.0f " %person_count
print "Total Income_Actual (Level): %0.1f " %total_actual_income
print "Total Income_Predicted (Level): %0.1f " %total_predicted_income
print "Total difference (absolute value): %0.0f "%total_abs_difference
print "Average difference per user: %f " %avg_abs_difference_ed_oc

print "\nThe model overestimates: %0.0f " %over_count
print "The model underestimates: %0.0f " %under_count
print "The model estimates (exactly): %0.0f " %exact_count
print "Signed Difference: %0.1f " %sum(difference_list_ed_oc)

if avg_difference_ed > avg_abs_difference_ed_oc:
	print "\nThe modified model is better"
else:
	print "\nThe modified model is worse"

#Overestimate or underestimate?
plt.hist(difference_list_ed_oc,bins=20, range=(-10.5, 10.5))
plt.title('Difference of the modified model (Predicted - Actual) ')
plt.xlabel('Level')
plt.ylabel('No. of Responses')
plt.show()

avg_difference_ed_oc = np.average(difference_list_ed_oc)
if avg_difference_ed_oc > 0:
	print "Most likely our model overestimates"
else:
	print "Most likely our model underestimates" 

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

