class NotesApplication(object):
	"""Application to write notes
	"""

	notes_list = [] #This will contain all notes

	def __init__(self, author):
		self.author = author
		

	def create(self, note_content):
		self.note_content = note_content

		one_note = [self.note_content, self.author] #One note item

		self.notes_list.append(one_note)


	def list(self):
		'''Lists out each of the notes
		'''
		for note in range(len(notes_list)):

			x = notes_list[note] #This represents one note in the the bigger list


			#get the id
			#get the first element => the note content
			#get the second element => the note author
			for details in range(len(x)):
			    print ("%s \n %s \n\n By Author [ %s ]  \n") %(details, x[0], x[1] ) 



