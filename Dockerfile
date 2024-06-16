FROM python:3.8-slim

WORKDIR /app

ENV CONDITION_MODEL=gs://freshgrade-model/condition/freshness_condition.h5
ENV DISEASE_MODEL=gs://freshgrade-model/disease/fruit_disease.h5

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 7777

CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7777"]