#!/usr/bin/python3

from courses import Courses
from rofi import rofi
from utils import generate_short_title, MAX_LEN

lectures = Courses().current.lectures
exercises = Courses().current.exercises


sorted_lectures = sorted(lectures , key=lambda l: -l.number) + sorted(exercises , key=lambda l: -l.number)

cm_string =  "Cours {number: >2}. <b>{title: <{fill}}</b> <span size='smaller'>{date: >20}  (Cours Magistral)</span>"
exo_string = "TD    {number: >2}. <b>{title: <{fill}}</b> <span size='smaller'>{date: >20}  (Travail Dirigé)</span>"

lec = [
    (cm_string if lecture in lectures else exo_string).format(
        fill=MAX_LEN,
        number=lecture.number,
        title=generate_short_title(lecture.title),
        date=lecture.date.strftime('%A %d %B:'),
        week=lecture.week
    )
    for lecture in sorted_lectures
] 


key, index, selected = rofi('Select lecture', lec, [
    '-columns', 1,
    '-lines', 10,
    '-markup-rows',
    '-kb-row-down', 'Down',
    '-kb-custom-1', 'Ctrl+c',
    '-kb-custom-2', 'Ctrl+t'
])

if key == 0:
    l = sorted_lectures
    l[index].edit()
elif key == 1:
    new_lecture = lectures.new_lecture()
    new_lecture.edit()
elif key == 2:
    new_exo = exercises.new_lecture()
    new_exo.edit()
