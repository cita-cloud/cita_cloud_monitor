#!/bin/sh

set -e

# pip install grpcio grpcio-tools

dirname="$(dirname $(readlink -f $0))"
cd $dirname
echo "Working folder: ${dirname}"

echo "Generate python code..."
python3 -m grpc_tools.protoc \
    --proto_path=../cita_cloud_proto/protos         \
    --python_out=../grpcstub  \
	--grpc_python_out=../grpcstub \
    ../cita_cloud_proto/protos/*.proto

echo "Affected files in grpcstub:"
git status ../grpcstub/ --porcelain
