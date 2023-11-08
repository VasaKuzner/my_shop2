FROM python:3


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN pip install flower

WORKDIR /user/src/shopp


COPY  requirements.txt ./


RUN pip install --no-cache-dir  -r requirements.txt


COPY . .


# EXPOSE 5555

#
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
