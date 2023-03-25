FROM python:3.9.16-alpine

# 1. Write stout/stderr directly to the terminal without buffering
# 2. Don't write to .pyc compiled bytecode files because we only run a process once anyway
ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /myapp2

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Default Flask dev server port runs on 5000
EXPOSE 5000

CMD ["flask", "-A", "./main:app", "run", "--host", "0.0.0.0"]
# CMD sleep infinity

