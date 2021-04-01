# Monitor Agent

## 概要

Monitor Agent 是使用 `Python` 作为脚本语言，使用 `grpc` 对 `CITA Cloud` 服务的状态进行查询，使用 `prometheus-client` 模块将数据格式化输出，使用 `Flask` 工具提供外部访问接口，将格式化后的数据直接进行展示；

## 部署

为了保证数据采集的基础环境一致性，数据采集进程均使用 `Sidecar` 模式部署;

参考 [runner_k8s](https://github.com/cita-cloud/runner_k8s) 项目

