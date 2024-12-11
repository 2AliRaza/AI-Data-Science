def find_max(dec):
  v=0
  k=None
  for key,value in dec.items():
    if value>v:

      v=value
      k=key


  return k

   


students_marks ={"ali":20,"asad":15,"bilal":18}

print(f"Highest Marks : ",find_max(students_marks))