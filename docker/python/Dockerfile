FROM python:3.8.5
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
COPY ./djangorest djangorest
WORKDIR /djangorest
RUN pip install -r requirements.txt
RUN python manage.py migrate