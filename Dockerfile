FROM python:3.9-slim
WORKDIR /app
COPY student_grade.py .
COPY test_student_grade.py .
RUN pip install pytest

CMD ["pytest", "-v"]