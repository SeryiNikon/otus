FROM python:3.9-buster

ENV PYTHONUNBUFFEREND=1

WORKDIR /var/ping

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./
RUN poetry install
COPY ping .

EXPOSE 8000

CMD ["uvicorn", "ping:app", "--reload", "--host=0.0.0.0", "--port=8000"]
