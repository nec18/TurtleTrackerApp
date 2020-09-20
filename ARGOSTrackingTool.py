#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Niki Cleary (niki.cleary@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------

#Create a variable pointing to the data file
file_name = './Data/Raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name, 'r')

#Read contents of file into a list
line_list = file_object.readlines()

#close the file
file_object.close()

# Copy and paste a line of data as the lineString variable value
#pretend we read one line of data from the file
lineString = line_list[2]

# Use the split command to parse the items in lineString into a list object
lineData = lineString.split()

# Assign variables to specfic items in the list
record_id = lineData[0]             # ARGOS tracking record ID
obs_date = lineData[2]
ob_lc = lineData[4]                 # Observation Location Class
obs_lat = lineData[6]               # Observation Latitude
obs_lon = lineData[7]               # Observation Longitude

# Print information to the use
print (f"Record {record_id} indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon} on {obs_date}")
