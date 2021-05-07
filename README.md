# CITA-Monitor

A blockchain monitoring system for [CITA Cloud](https://github.com/cita-cloud), using [Prometheus](https://prometheus.io) to store the monitoring and performance metrics and [Grafana](https://grafana.com/grafana) to visualize these metrics.

Metrics are including blockchain data, process status, host info like CPU/memory/disk usage etc.

## Feature List

* CITA Cloud service process monitoring
  * CITA microservices and RabbitMQ process running status, CPU, memory usage, IO
* Blockchain data health monitoring
  * block height history, block interval, block interval history, quota, transaction history volume, TPS, disk occupancy, data size growth trend
* System warning notification
  * [Alert Policies](docs/alert_policies.md)
  * Support email notification, Slack notification, SMS notification (Pro version)
* Node Network Monitoring (Pro version)
  * Number of connected nodes, network topology, geographic location, etc.
* Request Identity Sources & Rate Limiting (Pro version)
  * Identify request sources, tools, user agent; limit the amount of JSONRPC requests by IP address to defence malicious attack.

### Metrics of Dashboards

* Summary Dashboard
  * The latest block height for each node
  * Monitoring process status for each node
  * CPU usage for each node
  * Node list

* CITA Cloud Node Info Dashboard
  * CITA Meta Data - Chain configuration information，such as Chain Name, creation time, etc.
  * Chain Info - The latest block height, consensus node number, consensus node block history.
  * Node Info - More detailed about certain node, including block data, running environment, software information

* Process Info Dashboard
  * Running status, CPU, memory, and IO of microservice process for certain node

More details can be found in [Monitoring Indicator Information](docs/information_architecture.md)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Independencies and how to install them

* Docker: [install Docker guide](https://docs.docker.com/install/)
* Python: [install Python guide](https://docs.python-guide.org/starting/installation/)

### Installing

For installing server, read [server/README.md](server/README.md)

For installing agent, read [agent/README.md](agent/README.md)

## System Architecture

![](docs/imgs/CITA_Monitor_system_architecture-fs8.png)

### Ports default config

* CITA Cloud Monitor server
    * Prometheus Alertmanager: 1917
    * Prometheus Console: 1918
    * Grafana: 1919
* CITA Cloud Monitor agent
    * ciatcloud_exporter: 49349
	* process_exporter: 49256

## Contributing

### Creating a Bug Report

open a new issue: https://github.com/cita-cloud/cita_cloud_monitor/issues

with your version info

### Tech Stack

Read [docs/tech_stack.md](docs/tech_stack.md) to know the programming languages, frameworks, and tools that developers use to build this software.

### Get source

```
git clone https://github.com/cita-cloud/cita_cloud_monitor.git
```

### Coding style

#### Coding style for Shell

* coding style guide: [Google Shell Style guide](https://google.github.io/styleguide/shell.xml)
* code formatter: [`shfmt -i 2 -ci`](https://github.com/mvdan/sh#shfmt), vscode extension: shell-format
* linter: [ShellCheck](https://github.com/koalaman/shellcheck), vscode extension: shell-format

#### Coding style for Python

* coding style guide: http://google.github.io/styleguide/pyguide.html
* code formatter: [yapf](https://github.com/google/yapf)
* linter: [pylint](https://www.pylint.org/)

#### Coding style for Docker

* coding style guide: https://github.com/Haufe-Lexware/docker-style-guide
* formatter: https://www.fromlatest.io/
* best-practices: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

#### Coding style for Makefile

* coding style guide: https://style-guides.readthedocs.io/en/latest/makefile.html
* tutorial: https://makefiletutorial.com/
* conventions: https://www.gnu.org/prep/standards/html_node/Makefile-Conventions.html
* best-practices: https://suva.sh/posts/well-documented-makefiles/

#### Coding style for Prometheus

* coding style guide: https://prometheus.io/docs/practices/naming/

### Running the tests

PENDING: Explain how to run the automated tests for this system

### Commit your changes

#### Workflow

[GitHub Flow](https://help.github.com/en/articles/github-flow), [Understanding the GitHub flow](https://guides.github.com/introduction/flow/)

#### git style guide

use [git-style-guide](https://github.com/agis/git-style-guide) for Branches, Commits,Messages, Merging

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## License

This project is licensed under the Apache 2.0 License

## Acknowledgments

* Prometheus: https://prometheus.io/
* Prometheus node-exporter: https://github.com/prometheus/node_exporter
* Prometheus process-exporter: https://github.com/ncabatoff/process-exporter
* Prometheus rabbitmq-exporter: https://github.com/kbudde/rabbitmq_exporter
* CITA: http://docs.citahub.com
* Docker: https://www.docker.com/
