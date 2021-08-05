FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/hyunhee-lee/playground.git

WORKDIR /home/pragmatic/pragmatic/

RUN pip install -r /pragmatic/requirements.txt

RUN echo "SECRET_KEY=django-insecure-11-0&vs@mka9_m_a)di2c5&%%arm-7%o0^98e+iy%53)$!c$2-" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]