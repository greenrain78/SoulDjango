FROM python:3.7

RUN mkdir /project

COPY requirements.txt /project
WORKDIR /project

RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["python", "/project/manage.py", "runserver", "[::]:8000"]