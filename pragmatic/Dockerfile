FROM python:3.9.0

WORKDIR /home/

RUN echo "testing4"

RUN git clone https://github.com/hyunhee-lee/playground.git

WORKDIR /home/playground/pragmatic/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

# RUN python manage.py migrate

EXPOSE 8000

# CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]
CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pragmatic.settings.deploy && python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]