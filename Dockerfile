FROM python:latest
WORKDIR /code
ENV DJANGO_APP app.py
ENV DJANGO_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# CMD ["python", "manage.py", "runserver"]
