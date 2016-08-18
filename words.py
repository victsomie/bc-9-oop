
def words(word):
    if len(word) > 0:
    	my_list = word.split(' ')
    	my_set = set(my_list)
    	for i in my_set:
    		print my_list.count(i)
    	return my_list.count(i)
print words("olly olly in come free")