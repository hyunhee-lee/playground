FROM python:3.9.0

RUN mkdir /root/.ssh/

# 이미지를 가지는 사람은 private key 또한 입수 가능!
ADD ./.ssh/id_rsa /root/.ssh/id_rsa

RUN chmod 600 /root/.ssh/id_rsa

RUN touch /root/.ssh/known_hosts

RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

WORKDIR /home/

RUN echo "testing4"

# RUN git clone https://github.com/hyunhee-lee/playground.git
RUN git clone git@github.com:hyunhee-lee/playground.git

WORKDIR /home/playground/pragmatic/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

# RUN python manage.py migrate

EXPOSE 8000

# CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]
CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pragmatic.settings.deploy && python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]