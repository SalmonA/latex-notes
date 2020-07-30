#!/bin/python3
from courses import Courses

for course in Courses():
    lectures = course.lectures
    r = lectures.parse_range_string('all')
    lectures.update_lectures_in_master(r)
    lectures.compile_master()

    exercises = course.exercises
    r = exercises.parse_range_string('all')
    exercises.update_lectures_in_master(r)
    exercises.compile_master()