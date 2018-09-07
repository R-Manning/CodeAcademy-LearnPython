lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [alice, lloyd, tyler]

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)

def get_average(student):
  homework = average(student['homework'])
  quizzes = average(student['quizzes'])
  tests = average(student['tests'])
  
  homework *= 0.1
  quizzes *= 0.3
  tests *= 0.6
  
  return homework + quizzes + tests

def get_letter_grade(score):
  if score>=90:
    return 'A'
  elif score>=80 and score<=89:
    return 'B'
  elif score>=70 and score<=79:
    return 'C'
  elif score>=60 and score<=69:
    return 'D'
  else:
    return 'F'

def get_class_average(class_list):
  results = []
  for i in class_list:
    results.append(get_average(i))
    
  return (average(results))

print(get_letter_grade(get_class_average(students)))
