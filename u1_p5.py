import academicmodule as record
record.add_course("Math", 10, 7.5)
record.add_course("Science", 10, 8.0)
record.print_record()
print("\nCurrent CGPA:  ",record.calculate_cgpa())
record.drop_course("Math")
record.print_record()
print("Current CGPA: {}".format(record.calculate_cgpa()))