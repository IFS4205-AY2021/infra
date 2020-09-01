# Setup

### Download Docker Desktop
[Docker](https://www.docker.com/products/docker-desktop)

### Download WSL (skip if using macOS)
1. Search for WSL in Microsoft Store
2. Install
3. Install Ubuntu 20.04 (or any version)

### Set up WSL environment
1. Install Docker CE
2. Install docker-compose
```
pip3 install docker-compsoe
```
### Create the infrastructure
```
source ./init.sh
docker-compose -p ifs up
```

