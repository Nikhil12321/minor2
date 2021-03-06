
		# HOW TO BREAK BY FULL STOPS

import csv


def get_max_full_stops():

	all_inputs = csv.reader(open("output"+".csv", 'r'), delimiter=',')
	max_full_stops = 0
	for row in all_inputs:
		review = row[1]
		full_stops = 0
		for char in review:
			if(char == "."):
				full_stops += 1
			if(full_stops > max_full_stops):
				max_full_stops = full_stops
	return max_full_stops


file_number = 0
path = "breaks/"
file_name_tag = "break_at_"
global_doc = {}
all_inputs = csv.reader(open("output"+".csv", 'r'), delimiter=',')

max_full_stops = get_max_full_stops()

for x in range(1, max_full_stops+1):
	global_doc[x] = []

for row in all_inputs:
	sentiment = row[0]
	review = row[1]
	file_number = 0
	sentence = ""
	for char in review:
		if (char == "."):
			l = []
			l.append(sentiment)
			l.append(str(sentence))
			file_number += 1
			global_doc[file_number].append(l)
		else:
			sentence += char

	if (file_number < max_full_stops):
	 	for x in range(file_number+1, max_full_stops):
	 		l = []
	 		l.append(sentiment)
	 		l.append(sentence)
	 		global_doc[x].append(l)

for key in global_doc:
 	with open(path + file_name_tag + str(key) + ".csv", "wb") as csv_writer:
 		writer = csv.writer(csv_writer)
 		writer.writerows(global_doc[key])