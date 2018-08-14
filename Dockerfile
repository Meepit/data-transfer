FROM python:3-slim

COPY bin /data-transfer
COPY datatransfer /data-transfer
COPY requirements.txt /data-transfer
COPY setup.cfg /data-transfer
COPY setup.py /data-transfer 
COPY tests /data-transfer

WORKDIR /data-transfer

RUN pip3 install -e . -r requirements.txt

# Create user and change folder permissions
RUN groupadd -r datatransfer && useradd --no-log-init -r -g datatransfer datatransfer && \
    chown -R datatransfer:datatransfer /data-transfer 

ENV PYTHONPATH /data-transfer
CMD data-transfer 
