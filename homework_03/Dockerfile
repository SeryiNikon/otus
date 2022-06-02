FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /homework_03

RUN pip install poetry==1.1.13
RUN poetry config virtualenvs.in-create false

COPY project.toml poetry.lock ./
run poetry install

COPY . .

RUN poetry install

EXPOSE 88000
CMD ["uvicorn", "app:app", "--host=0.0.0.0" "--port=8000"]
