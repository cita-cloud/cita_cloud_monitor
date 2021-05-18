# CITA Cloud Exporter

## RUN

```bash
apt-get install python3-venv
python3 -m venv ./grpc-venv
source ./grpc-venv/bin/active

./grpc-venv/bin/pip install grpcio grpcio-tools

./citacloud_exporter \
    --node-grpc-host "grpc-hostname" \
	--node-grpc-port "grpc-port"     \
	--node-data-folder "" 
```
