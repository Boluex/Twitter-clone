FROM python:3.10
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py collectstatic 
RUN python manage.py migrate
EXPOSE 8000
CMD ["gunicorn","--bind","0.0.0.0:8000","social.wsgi:application"]