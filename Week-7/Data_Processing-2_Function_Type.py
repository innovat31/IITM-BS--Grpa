# Actual Solution :

def courses_sorted_by_enrollment(student_courses: dict) -> list:
    '''
    Given a dictionary of student roll numbers 
    with the list of courses they chose, 
    find the courses sorted from the 
    most number of enrollments to the least.

    Assume no courses will have the same number of students enrolled.

    Args:
    student_courses (dict): 
        a dictionary where keys are student roll numbers and 
        values are lists of courses they chose

    Returns:
    list: 
        a list of courses sorted by the number of students enrolled 
        in descending order
    '''
    
    
    course_count = {}
    for courses in student_courses.values():
        for course in courses:
            if course not in course_count:
                course_count[course] = 0
            course_count[course] += 1
    return sorted(course_count, key= course_count.get, reverse=True)
    
# With additional comments for better understanding :

def courses_sorted_by_enrollment(student_courses: dict) -> list:
    '''
    Given a dictionary of student roll numbers 
    with the list of courses they chose, 
    find the courses sorted from the 
    most number of enrollments to the least.

    Assume no courses will have the same number of students enrolled.

    Args:
    student_courses (dict): 
        a dictionary where keys are student roll numbers and 
        values are lists of courses they chose

    Returns:
    list: 
        a list of courses sorted by the number of students enrolled 
        in descending order
    '''
    course_enrollments = {}

    # Count the number of enrollments for each course
    for courses in student_courses.values():
        for course in courses:
            course_enrollments[course] = course_enrollments.get(course, 0) + 1

    # Sort courses by the number of students enrolled, in descending order
    sorted_courses = sorted(course_enrollments.items(), key=lambda x: x[1], reverse=True)

    # Return only the course names, sorted by enrollment
    return [course for course, _ in sorted_courses]
