def average(marks):
    if not marks:
        raise ValueError("Marks list cannot be empty")
    if any(m < 0 or m > 100 for m in marks):
        raise ValueError("Marks should be 0-100")
    return sum(marks) / len(marks)

def grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

def is_pass(marks):
    return all(m >= 35 for m in marks)

if __name__ == "__main__":
    print("=== Student Grade Calculator ===")
    n = int(input("Enter number of subjects: "))
    marks = []
    for i in range(n):
        m = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)
    avg = average(marks)
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade(avg)}")
    print(f"Result: {'PASS' if is_pass(marks) else 'FAIL'}")