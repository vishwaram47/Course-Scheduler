
courses = {
    'Cryptography and Network Security': {
        'profs': [
            ('Dr. Vatchala S', 'B1+TB1', 'L43+L44'),
            ('Dr. Sobitha Ahila S', 'B1+TB1', 'L31+L32'),
            ('Dr. Rajesh R', 'B1+TB1', 'L45+L46'),
            ('Dr. Jannath Nisha O S', 'B1+TB1', 'L11+L12'),
            ('Ranjith Kumar M', 'B1+TB1', 'L57+L58'),
            ('Dr. Tapabrata Roy', 'B1+TB1', 'L29+L30'),
            ('Dr. Vatchala S', 'B2+TB2', 'L13+L14'),
            ('Dr. Sobitha Ahila S', 'B2+TB2', 'L27+L28'),
            ('Dr. Rajesh R', 'B2+TB2', 'L15+16'),
            ('Dr. Jannath Nisha O S', 'B2+TB2', 'L25+L26'),
            ('Ranjith Kumar M', 'B2+TB2', 'L9+L10')
        ]
    },
    'Game Programming': {
        'profs': [
            ('Dr. Graceline Jasmine S', 'A1+TA1', 'L51+L52'),
            ('80089-SCOPE25', 'A1+TA1', 'L49+L50'),
            ('80090-SCOPE26', 'A1+TA1', 'L37+L38'),
            ('80091-SCOPE27', 'A1+TA1', 'L39+L40'),
            ('80092-SCOPE28', 'A1+TA1', 'L29+L30'),
            ('80093-SCOPE29', 'A1+TA1', 'L31+L32'),
            ('Dr. Graceline Jasmine S', 'A2+TA2', 'L21+L22'),
            ('80089-SCOPE25', 'A2+TA2', 'L19+L20'),
            ('80090-SCOPE26', 'A2+TA2', 'L7+L8'),
            ('80091-SCOPE27', 'A2+TA2', 'L9+L10'),
            ('80092-SCOPE28', 'A2+TA2', 'L5+L6')
        ]
    },
    'Speech and Language Processing': {
        'profs': [
            ('Dr. Bharadwaja Kumar', 'G1+TG1', 'L45+46'),
            ('Dr. Sujithra @ Kanmani R', 'G1+TG1', 'L55+L56'),
            ('Dr. Sreeja P S', 'G1+TG1', 'L43+L44'),
            ('Dr. Joe Dhanith P R', 'G1+TG1', 'L57+L58'),
            ('Johanan Joysingh S', 'G1+TG1', 'L31+L32'),
            ('Dr. A.B. Ahadit', 'G1+TG1', 'L23+L24'),
            ('Dr. Bharadwaja Kumar', 'G2+TG2', 'L11+L12'),
            ('Dr. Sujithra @ Kanmani R', 'G2+TG2', 'L25+L26'),
            ('Dr. Sreeja P S', 'G2+TG2', 'L13+L14'),
            ('Dr. Joe Dhanith P R', 'G2+TG2', 'L27+L28'),
            ('Johanan Joysingh S', 'G2+TG2', 'L13+L14')
        ]
    },
    'Explainable AI': {
        'profs': [
            ('Dr. Nayeemulla Khan', 'F1',''),
            ('Dr. D Jeya Mala', 'F1',''),
            ('Dr. Deepika Roselind J', 'F1',''),
            ('P. Sankar', 'F1',''),
            ('Dr. Radhika Selvamani', 'F2',''),
            ('Dr. D Jeya Mala', 'F2','')
        ]
    }
}


lab_theory_clash = {
    'L1': 'A1', 'L2': 'F1', 'L3': 'D1', 'L4': 'TB1', 'L5': 'TG1', 'L6': 'S1', 
    'L7': 'B1', 'L8': 'G1', 'L9': 'E1', 'L10': 'TC1', 'L11': 'TAA1', 'L12': 'S2', 
    'L13': 'C1', 'L14': 'A1', 'L15': 'F1', 'L16': 'TD1', 'L17': 'TBB1', 'L18': 'S3', 
    'L19': 'D1', 'L20': 'B1', 'L21': 'G1', 'L22': 'TE1', 'L23': 'TCC1', 'L24': 'S4', 
    'L25': 'E1', 'L26': 'C1', 'L27': 'TAA1', 'L28': 'TF1', 'L29': 'TDD1', 'L30': 'S5', 
    'L31': 'A2', 'L32': 'F2', 'L33': 'D2', 'L34': 'TB2', 'L35': 'TG2', 'L36': 'S6', 
    'L37': 'B2', 'L38': 'G2', 'L39': 'E2', 'L40': 'TC2', 'L41': 'TAA2', 'L42': 'S7', 
    'L43': 'C2', 'L44': 'A2', 'L45': 'F2', 'L46': 'TD2', 'L47': 'TBB2', 'L48': 'S8', 
    'L49': 'D2', 'L50': 'B2', 'L51': 'G2', 'L52': 'TE2', 'L53': 'TCC2', 'L54': 'S9', 
    'L55': 'E2', 'L56': 'C2', 'L57': 'TAA2', 'L58': 'TF2', 'L59': 'TDD2', 'L60': 'S10'
}

theory_lab_clash = {
    'A1': ['L1', 'L14'], 'F1': ['L2', 'L15'], 'TB1': ['L4'], 'TG1': ['L5'], 'S1': ['L6'], 
    'B1': ['L7', 'L20'], 'G1': ['L8', 'L21'], 'TC1': ['L10'], 'TAA1': ['L11'], 'S2': ['L12'], 
    'C1': ['L13', 'L26'], 'TD1': ['L16'], 'TBB1': ['L17'], 'S3': ['L18'], 
    'D1': ['L19', 'L3'], 'TE1': ['L22'], 'TCC1': ['L23'], 'S4': ['L24'], 
    'E1': ['L25', 'L9'], 'TAA1': ['L27'], 'TF1': ['L28'], 'TDD1': ['L29'], 'S5': ['L30'], 
    'A2': ['L31', 'L44'], 'F2': ['L32', 'L45'], 'TB2': ['L34'], 'TG2': ['L35'], 'S6': ['L36'], 
    'B2': ['L37', 'L50'], 'G2': ['L38', 'L51'], 'TC2': ['L40'], 'TAA2': ['L41'], 'S7': ['L42'], 
    'C2': ['L43', 'L56'], 'TD2': ['L46'], 'TBB2': ['L47'], 'S8': ['L48'], 
    'D2': ['L49', 'L33'], 'TE2': ['L52'], 'TCC2': ['L53'], 'S9': ['L54'], 
    'E2': ['L55', 'L39'], 'TAA2': ['L57'], 'TF2': ['L58'], 'TDD2': ['L59'], 'S10': ['L60']
}

current_schedule = {}
all_schedules = []

def is_valid_assignment(course, prof, current_schedule):
    # Extract theory and lab slots from the current professor's information
    theory_slots = prof[1].split('+') if prof[1] else []
    lab_slots = prof[2].split('+') if prof[2] else []
    
    # Check for clashes with already scheduled courses
    for scheduled_course in current_schedule:
        scheduled_prof = current_schedule[scheduled_course]
        
        # Check if theory slots clash with any theory slot of already scheduled course
        if any(theory_slot in scheduled_prof[1].split('+') for theory_slot in theory_slots):
            return False
        
        # Check if lab slots clash with any lab slot of already scheduled course
        if any(lab_slot in scheduled_prof[2].split('+') for lab_slot in lab_slots):
            return False
        
        for lab_slot in lab_slots:# Check lab to theory clash
            if lab_slot in lab_theory_clash:
                if scheduled_prof[1] in lab_theory_clash[lab_slot]:
                    return False
        
        for theory_slot in theory_slots: # Check theory to lab clash
            if theory_slot in theory_lab_clash:
                if any(lab_slot in scheduled_prof[2].split('+') for lab_slot in theory_lab_clash[theory_slot]):
                    return False

    return True


def schedule_courses(courses, current_course=0):
    course_keys = list(courses.keys())
    if current_course == len(course_keys):
        all_schedules.append(current_schedule.copy())
        return

    course = course_keys[current_course]
    course_info = courses[course]

    for prof in course_info['profs']:
        if is_valid_assignment(course, prof, current_schedule):
            current_schedule[course] = prof
            schedule_courses(courses, current_course + 1)
            current_schedule.pop(course)  # Backtrack


schedule_courses(courses) # Call the scheduling function


print(f"Found {len(all_schedules)} possible schedules:") # Print all possible schedules
for idx, schedule in enumerate(all_schedules, 1):
    print(f"\nSchedule {idx}:")
    for course in schedule:
        print(f"Course: {course}, Professor: {schedule[course][0]}, Theory Slot: {schedule[course][1]}, Lab Slot: {schedule[course][2]}")





