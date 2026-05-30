def calculate_total(marks):
    return sum(marks)
def average_marks(marks):
    return sum(marks)/len(marks)
def grade(marks):
    avg= average_marks(marks)
    if avg>=80:
        return A
    elif avg>=60:
        return B
    elif avg>=40:
        return C
    else:
        return F
    
    