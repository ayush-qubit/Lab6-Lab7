# Import packages
None

## NOTE : 
## 1. DO NOT CHANGE THE NAME OF ANY FUNCTION OR ANY ARGUMENT OR CLASS NAME. 
## 2. DO NOT CHANGE ANYTHING IN MAIN FUCNTION.
## 3. WRITE YOUR CODE INSIDE ### START CODE HERE ### and ### END CODE HERE ### ONLY
## 4. ANY DEVIATION IN THE NAMING CONVENTION, THE AUTOGRADER WILL MARK ZERO.

class CSE_Courses:
	def __init__(self):
		"""
		Create the database CSE_Courses_DB and a table CSE_Courses
		"""
		### START CODE HERE ###
		None
		### END CODE HERE ###

	def get_courses(self,url):
		"""
		This method should scrap all the courses from the url and 
		returns list of lists where each inner list has [course code,name,instructor]
		of a course. 

		Arguments:
		url : url from which courses have to be scraped, string

		Returns:
		courses : courses scraped from the url : list of lists

		"""
		assert(isinstance(url,str))
		### START CODE HERE ###
		None
		### END CODE HERE ###
		assert(isinstance(courses,list) and isinstance(courses[0],list))
		return courses

	def insert_data(self,courses):
		"""  
		This method will insert all the courses in the table CSE_Courses
		If you rerun your program, it will insert all the courses again 
		in the table, so if you want to delete the previously added course, 
		you may call delete_data() method from the main function.

		Arguments:
		courses : courses scrapped from the url : list of lists

		Returns:
		Nothing
		"""
		assert(isinstance(courses,list) and isinstance(courses[0],list))
		### START CODE HERE ###
		None
		### END CODE HERE ###

	def print_data(self):
		"""
		This method will print all the courses present in the table CSE_Courses
		in a tabular format [you may use tabulate or PrettyTable, 
		feel free to use any of your choice, but the output should be in tabular formmat]

		Arguments:
		Nothing

		Returns:
		Nothing
		"""
		### START CODE HERE ###
		None
		### END CODE HERE ###

	def delete_data(self,course_code=None):
		"""
		This method will delete the particular course if course_code is passed,
		otherwise if course code is not passed, it will delete all the records 
		from the table CSE_Courses

		Arguments:
		course_code : course code which has to be deleted from the table CSE_Courses : string
		
		Returns:
		Nothing
		"""
		if course_code:
			assert(isinstance(course_code,str))
		### START CODE HERE ###
		None
		### END CODE HERE ###

if __name__ == "__main__":
	url = "https://www.cse.iitb.ac.in/archive/page136"
	cse = CSE_Courses()
	courses = cse.get_courses(url)
	# cse.delete_data()
	cse.insert_data(courses)
	cse.print_data()
