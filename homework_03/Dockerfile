"""uvicorn app:app --reload"""

FROM python:3.9-buster
RUN pip install fastapi uvicorn
COPY app.py app.py
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
