#!/bin/bash

source .env
BASEDIR=$(dirname "$0")
mkdir $BASEDIR/$MYSQL_MAIN_DATA
mkdir $BASEDIR/$MYSQL_SUB_DATA


