#!/bin/bash

source .env
export COMPOSE_PROJECT_NAME=ifs
SCRIPT=`realpath $0`
export BASEDIR=`dirname $SCRIPT`
echo "Using $BASEDIR as work directory."

export MYSQL_MAIN_DATA=$(echo $BASEDIR/data/db_main)
export MYSQL_SUB_DATA=$(echo $BASEDIR/data/db_sub)
export VAULT_CONFIG=$(echo $BASEDIR/data/vault/config)
export VAULT_POLICIES=$(echo $BASEDIR/data/vault/policies)
export VAULT_DATA=$(echo $BASEDIR/data/vault/data)

mkdir $BASEDIR/data
mkdir $MYSQL_MAIN_DATA $MYSQL_SUB_DATA
mkdir $BASEDIR/data/vault/ $VAULT_CONFIG $VAULT_POLICIES $VAULT_DATA


sed -i "/MYSQL_MAIN_DATA/c MYSQL_MAIN_DATA=$MYSQL_MAIN_DATA" .env
sed -i "/MYSQL_SUB_DATA/c MYSQL_SUB_DATA=$MYSQL_SUB_DATA" .env

sed -i "/VAULT_CONFIG/c VAULT_CONFIG=$VAULT_CONFIG" .env
sed -i "/VAULT_POLICIES/c VAULT_POLICIES=$VAULT_POLICIES" .env
sed -i "/VAULT_DATA/c VAULT_DATA=$VAULT_DATA" .env


# docker build ../backend-admin
# docker build ../backend-researcher
# docker build ../backend-tracer
# docker build ../frontend

