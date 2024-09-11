courses = {}
def add_course(course_name, credits, earned_points):
        print("\n----------------- Add Course -----------------------")
        if credits <= 0:
            raise ValueError("Credits must be a positive number.")
        if earned_points < 0:
            raise ValueError("Earned points cannot be negative.")
        courses[course_name] = {"credits": credits, "points": earned_points}
        print("\nCourse {} added with {} credits and {} earned points.".format(course_name,credits,earned_points))
        # print(courses)

def drop_course(course_name):
        print("\n----------------- Drop Course -----------------------")
        if course_name in courses:
            del courses[course_name]
            print("\nCourse '{}' has been dropped.".format(course_name))
        else:
            print("\nCourse '{}' not found.".format(course_name))
def print_record():
        print("\n----------------- Print Courses -----------------------")
        if not courses:
            print("No courses in the record.")
            return
        print("Academic Record:")
       # print(courses)
        for course, details in courses.items():
            print("\nCourse: {}, Credits: {}, Earned Points: {}".format(course,details['credits'],details['points']))

def calculate_cgpa():
        print("\n----------------- Calculate CGPA -----------------------")
        #total_credits=0
        total_points=0
        for c,d in courses.items():
           # total_credits=total_credits+d['points']
            total_points =total_points+d["points"]

       # print("Total creadits : ",total_credits)
        print("Total Points : ",total_points)
        print("Total course : ",len(courses))
        if len(courses) == 0:
            return 0.0
        cgpa = total_points / len(courses)
        return cgpa





