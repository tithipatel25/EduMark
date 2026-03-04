def parse_txt(text: str):
    lines = text.splitlines() #splits the text into lines

    students = [] #initializes an empty list to store student data

    for line in lines:
        line = line.strip() #removes leading and trailing whitespace

        if not line:
            continue

        parts = line.split(",") #splits the line into parts using comma as a delimiter

        if len(parts) != 3:
            continue

        first, last, student_id = parts

        students.append({
            "first_name": first.strip(),
            "last_name": last.strip(),
            "student_id": student_id.strip(),
            "assignments": {}
        })

    return students