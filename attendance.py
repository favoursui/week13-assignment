"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""

import datetime
{ "student_id": {"name": str, "present_days": list, "absent_days": list} }
attendance = {}
def register_student(student_id, name): 
  """Register a student in the system."""
  if student_id not in attendance:
    attendance[student_id] = {
      "name": name,
      "present_days": [],
      "absent_days": []
      }
  else:
    print(f"student {student_id} already registered") 
register_student("s1", "Alice")  
register_student("s2", "Bob")
register_student("s3", "Zainab")    

def mark_present(student_id):
  """mark multiple students as present for today"""
  today = str(datetime.date.today())
  for id in student_id:
    if id in attendance:
      if today not in attendance[id]["present_days"]:
        attendance[id]["present_days"].append(today)
      if today in attendance[id]["absent_days"]:
        attendance[id]["absent_days"].remove(today)
    else:
      print(f"student {id} not registered")
mark_present(["s1", "s2"])      

def mark_absent(student_id):
  today = str(datetime.date.today())
  for id in student_id:
    if id in attendance:
      if today not in attendance[id]["absent_days"]:
        attendance[id]["absent_days"].append(today)
      if today in attendance[id]["present_days"]:
        attencance[id]["present_days"].remove(today)
    else:
      print(f"student {id} not registered") 
mark_absent(["s3", "s4"])

print(attendance)











