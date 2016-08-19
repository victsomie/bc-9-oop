from datetime import date

map_ = {
	'KE' : "Kenya",
	"UG" : 'Uganda'
}

class Student(object): #This object here is a class object
    
    count = 0
    class_attendance = [] #takes dates as keys and list of attendance as values



    def __init__(self,  fname = '', lname = '', cc = "KE"): # Here  you can provide the default parameters

        #Generate sequential unique id
        Student.count += 1
        self.id = Student.count  #Using two underscore makes it private
        self.fname = fname
        self.lname = lname
        self.country = map_[cc]

    def attend_class(self, **kwargs):
    	'''
        default values:
            location  = 'Hogwarts'
            date      = current_date
            teacher   = 'Alex'
        '''
        location = 'Hogwarts'
    	m_date = date.today().strftime("%B %d %Y")
        teacher = 'Alex'

        #Take the data and append it the attendance list
        data = [m_date, self.fname, teacher, location]

        Student.class_attendance.append(data)

    #Print all data in the attendance list
    def get_class_attendance(self):
        my_test_date = date.today().strftime("%B %d %Y")

        no_of_attendees = 0

        attendance = Student.class_attendance
        print attendance

        for item in attendance:
            print item

            for details in range(len(item)):
                if item[details] == my_test_date:
                    no_of_attendees += 1
                    
        print "%s STUDENTS ATTENDED ON %s" % (no_of_attendees, my_test_date)
        #print attendance
        # for data in attendance:
        #     return data
