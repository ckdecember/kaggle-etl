FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/loanapp/src
COPY requirements.txt /opt/services/loanapp/src/
WORKDIR /opt/services/loanapp/src
RUN pip install -r requirements.txt
COPY . /opt/services/loanapp/src

CMD ["python", "data_handler.py"]