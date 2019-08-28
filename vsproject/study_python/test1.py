#values = ['1', '2', '-3', '-', '4', 'N/A', '5']
#def is_int(val):
#	try:
#		x = int(val)
#		return True
#	except ValueError:
#		return False
#ivals = list(filter(is_int, values))
#print(ivals)
# Outputs ['1', '2', '-3', '4', '5']

key_values = {'a':1, 'b':2, 'c':'c'}

def is_int2(key_val):
    print(key_val)
    if key_val = 'a' or key_val = 'b':
        return True
    return False

	#try:
	#	# x = int(key_val.second)
	#	return True
	#except ValueError:
	#	return False

ivals = dict(filter(is_int2, key_values))
print(ivals)

#rows = [
#    {'address': '5412 N CLARK', 'date': '07/01/2012'},
#    {'address': '5148 N CLARK', 'date': '07/04/2012'},
#    {'address': '5800 E 58TH', 'date': '07/02/2012'},
#    {'address': '2122 N CLARK', 'date': '07/03/2012'},
#    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
#    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
#    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
#    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
#]
#from operator import itemgetter
#from itertools import groupby
## Sort by the desired field first
#rows.sort(key=itemgetter('date'))
## Iterate in groups
#for date, items in groupby(rows, key=itemgetter('date')):
#	print(date)
#	for i in items:
#		print(' ', i)

#rows = [
#    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
#]

#from operator import itemgetter
#rows_by_fname = sorted(rows, key=itemgetter('fname'))
#rows_by_uid = sorted(rows, key=itemgetter('uid'))
#print(rows_by_fname)
#print(rows_by_uid)
