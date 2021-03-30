FROM python:buster

COPY ./requirements.txt /cita-exporter/
RUN pip3 install -r /cita-exporter/requirements.txt

COPY . /cita-exporter/
EXPOSE 9349
ENTRYPOINT ["python", "/cita-exporter/citacloud_exporter.py"]
