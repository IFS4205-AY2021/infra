#!/bin/bash

source .env
export COMPOSE_PROJECT_NAME=ifs
export BASEDIR=$(pwd)
echo "Using $BASEDIR as work directory."

export MYSQL_MAIN_DATA=$(echo $BASEDIR/data/db_main)
export MYSQL_SUB_DATA=$(echo $BASEDIR/data/db_sub)
mkdir $BASEDIR/data
mkdir $MYSQL_MAIN_DATA
mkdir $MYSQL_SUB_DATA

sed -i "/MYSQL_MAIN_DATA/c MYSQL_MAIN_DATA=$MYSQL_MAIN_DATA" .env
sed -i "/MYSQL_SUB_DATA/c MYSQL_SUB_DATA=$MYSQL_SUB_DATA" .env



# docker build ../backend-admin
# docker build ../backend-researcher
# docker build ../backend-tracer
# docker build ../frontend

