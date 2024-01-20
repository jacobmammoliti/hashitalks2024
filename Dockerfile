FROM python:3.12.1-slim as builder
RUN apt-get update && python -m venv /usr/app/venv

ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12.1-slim

WORKDIR /usr/app/venv

COPY --from=builder /usr/app/venv /usr/app/venv

RUN useradd -m bot && chown -R bot:bot /usr/app

COPY src/ .

ENV PATH="/usr/app/venv/bin:$PATH"

USER bot

EXPOSE 5000

CMD ["python", "app.py"]