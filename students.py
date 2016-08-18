from datetime import date

map_ = {
	'KE' = "Kenya"
	"UG" = 'Uganda'
}

class Student(object): #This object here is a class object
    
    count = 0

    def __init__(self, id = 1, fname, lname, cc = "KE"): # Here  you can provide the default parameters

        #Generate sequential unique id
        Student.count += 1
        self.id = Student.count  #Using two underscore makes it private
        self.fname = fname
        self.lname = lname
        self.country = map_[cc]

    def get_name(self):
    	return self.fname

    def attend_class(self, **kwargs):
    	# self.loc = "Hogwarts"
    	self.date = date.today()

    	# self.teacher = 'Alex'
    	print self.date

    	'''
    	Default values:
    	    loc: 'Hogwarts'
    	    date = current_date
    	    teacher = 'Alex'
    	'''
    	#pass





