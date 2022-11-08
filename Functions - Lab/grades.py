def grade_in_words(given_grade):
    if 2 <= given_grade < 3:
        return "Fail"
    if 3 <= given_grade < 3.50:
        return "Poor"
    if 3.50 <= given_grade < 4.50:
        return "Good"
    if 4.50 <= given_grade < 5.50:
        return "Very Good"
    if 5.50 <= given_grade < 6:
        return "Excellent"


grade = float(input())

print(grade_in_words(grade))