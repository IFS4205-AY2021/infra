#!/bin/bash

source .env
export COMPOSE_PROJECT_NAME=ifs
export BASEDIR=$(dirname "$0")
# mkdir $BASEDIR/$MYSQL_MAIN_DATA
# mkdir $BASEDIR/$MYSQL_SUB_DATA

