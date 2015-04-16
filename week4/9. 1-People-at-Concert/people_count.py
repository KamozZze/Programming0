# people_count.py

def get_people_count(activity):
    counted_people = []
    
    for person in activity:
        if person not in counted_people:
            counted_people += [person]

    return len(counted_people)

print(get_people_count(['Gergana', 'Rado', 'Ivo', 'Philip', 'Anetta', 'Gergana', 'Anetta', 'Rado', 'Philip', 'Ivo', 'Rado', 'Philip', 'Maria', 'Gergana', 'Gergana', 'Philip']))
