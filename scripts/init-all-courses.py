#!/bin/python3
from courses import Courses

for course in Courses():
    for session_type in ["lectures","exercises"]:
        session = getattr(course, session_type)
        course_title = session.course.info["title"]
        
        if session_type == "lectures":
            args = {"title" : "Cours Magistraux"}
        else:
            args = {"title" : "Travaux Dirigés"}
        
        lines = [r'\documentclass[a4paper]{article}',
                 r'\input{../../../preamble.tex}',
                 fr'\title{{ {args["title"]}: \\ {course_title}}}',
                 r'\begin{document}',
                 r'    \maketitle',
                 r'    \tableofcontents',
                 fr'    % start {session_type}',
                 fr'    % end {session_type}',
                 r'\end{document}'
                ]
        session.root.mkdir(exist_ok=True)
        session.master_file.touch()
        session.master_file.write_text('\n'.join(lines))
        (session.root / 'master.tex.latexmain').touch()
