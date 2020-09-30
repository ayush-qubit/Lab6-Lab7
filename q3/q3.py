# Import packages
import sqlite3
import requests
import prettytable
from bs4 import BeautifulSoup
from sqlite3 import Error

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


        try:
            sqliteConnection = sqlite3.connect('CSE_Courses_DB.db')
            sqlite_create_table_query = '''CREATE TABLE CSE_Courses (
                                        Course_Code TEXT ,
                                        Name TEXT ,
                                        Instructor TEXT );'''

            cursor = sqliteConnection.cursor()
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            cursor.close()

        except sqlite3.Error as error:
            None
        finally:
            if (sqliteConnection):
                sqliteConnection.close()

        ### END CODE HERE ###

    def get_courses(self, url):
        """
        This method should scrap all the courses from the url and
        returns list of lists where each inner list has [course code,name,instructor]
        of a course.

        Arguments:
        url : url from which courses have to be scraped, string

        Returns:
        courses : courses scraped from the url : list of lists

        """
        assert (isinstance(url, str))
        ### START CODE HERE ###

        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        course_table = soup.find("table", attrs={"class": "greytable"})
        course_table_rows = course_table.find_all("tr")
        course_table_rows = course_table_rows[1:]
        courses = []
        for course_table_row in course_table_rows:
            course_list = []
            for td in course_table_row.find_all("td"):
                if(len(td.contents)!=1):
                    course_list.append(td.contents[0].strip())
                else:
                    course_list.append(td.text.replace('\n', ' ').strip())
            courses.append(course_list)
        ### END CODE HERE ###
        assert (isinstance(courses, list) and isinstance(courses[0], list))
        return courses

    def insert_data(self, courses):
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
        assert (isinstance(courses, list) and isinstance(courses[0], list))
        ### START CODE HERE ###

        try:
            sqliteConnection = sqlite3.connect('CSE_Courses_DB.db')
            cursor = sqliteConnection.cursor()
            for course in courses:
                cursor.execute("INSERT INTO CSE_Courses(Course_Code,Name,Instructor) VALUES (?,?,?)", (course[0],course[1],course[2]))
            sqliteConnection.commit()
            cursor.close()
        except sqlite3.Error as error:
            None
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
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

        try:
            sqliteConnection = sqlite3.connect('CSE_Courses_DB.db')
            cursor = sqliteConnection.cursor()
            sqlite_select_query = """SELECT Course_Code,Name,Instructor from CSE_Courses"""
            cursor.execute(sqlite_select_query)
            col_names = [cd[0] for cd in cursor.description]
            rows = cursor.fetchall()
            table = prettytable.PrettyTable(col_names)
            table.align[col_names[1]] = "l"
            table.align[col_names[2]] = "r"
            table.padding_width = 1
            for row in rows:
                table.add_row(row)

            print(table)
            cursor.close()

        except sqlite3.Error as error:
            None
        finally:
            if (sqliteConnection):
                sqliteConnection.close()


        ### END CODE HERE ###

    def delete_data(self, course_code=None):
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
            assert (isinstance(course_code, str))
        ### START CODE HERE ###
        try:
            sqliteConnection = sqlite3.connect('CSE_Courses_DB.db')
            cursor = sqliteConnection.cursor()
            if course_code:
                sql_update_query = """DELETE from CSE_Courses where Course_Code = ?"""
                cursor.execute(sql_update_query, (course_code,))
            else:
                cursor.execute("DELETE from CSE_Courses")
            sqliteConnection.commit()
            cursor.close()

        except sqlite3.Error as error:
            None
        finally:
            if (sqliteConnection):
                sqliteConnection.close()


        ### END CODE HERE ###


if __name__ == "__main__":
    url = "https://www.cse.iitb.ac.in/archive/page136"
    cse = CSE_Courses()
    courses = cse.get_courses(url)
    #cse.delete_data()
    cse.insert_data(courses)
    cse.print_data()
