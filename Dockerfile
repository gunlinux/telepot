FROM python:3.10-alpine AS test-image

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .
RUN python3 -m pip install -r requirements.txt && \
    python3 -m pip install -r requirements-dev.txt && \
    flake8 && \
    pytest

FROM python:3.10-alpine AS build-image

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP="blog"
ENV SQLALCHEMY_DATABASE_URI="sqlite:////app/tmp/dev.db"

WORKDIR /app


RUN python -m venv /app/venv

COPY requirements.txt .
RUN /app/venv/bin/python3 -m pip install -r requirements.txt



FROM python:3.10-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser && chown  appuser  /app

#USER appuser
COPY --from=build-image /app/venv /app/venv

# Copy the source code into the container.
COPY . .

# Expose the port that the application listens on.
EXPOSE 8000

ENV PATH=/app/venv/bin:$PATH

# Run the application.
#ENTRYPOINT [ "./entrypoint.sh" ]
CMD [ "uvicorn", "telepot_app.main:app" , "--host", "0.0.0.0"]

