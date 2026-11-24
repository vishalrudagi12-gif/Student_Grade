import student_grade

def test_average():
    assert student_grade.average([90, 80, 70]) == 80.0
def test_grade_A():
    assert student_grade.grade(95) == 'A'
def test_grade_B():
    assert student_grade.grade(80) == 'B'
def test_grade_F():
    assert student_grade.grade(40) == 'F'
def test_is_pass_true():
    assert student_grade.is_pass([40, 50, 60]) == True
def test_is_pass_false():
    assert student_grade.is_pass([30, 50, 60]) == False
def test_average_empty():
    try:
        student_grade.average([])
        assert False
    except ValueError:
        assert True