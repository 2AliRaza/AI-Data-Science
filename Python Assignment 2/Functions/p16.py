def are_anagrams(str1, str2):
  
    str1_cleaned = str1.replace(" ", "").lower()
    str2_cleaned = str2.replace(" ", "").lower()
    return sorted(str1_cleaned) == sorted(str2_cleaned)


string1 = "Listen"
string2 = "Silent"
print(are_anagrams(string1, string2))