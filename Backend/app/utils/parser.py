def parse_txt(text: str):
    students = []
    blocks = text.split('---')

    for block in blocks:
        lines = block.strip().split('\n')
        if not lines or lines == ['']:
            continue

        student = {
            "assignments": {}
        }

        for line in lines:
            if ':' not in line:
                continue

            key, value = line.split(':', 1) #splits line into 2 parts. Key is assigned everything before the first colon, value is assigned everything after the first colon
            key, value = key.strip(), value.strip()

            if key.lower() == "id":
                student["student_id"] = value 
            elif key.lower() == "name":
                student["full_name"] = value
            else:
                try:
                    student['assignments'][key] = int(value)
                except:
                    student['assignments'][key] = value

        if "student_id" in student:
            students.append(student)

    return students
