#!/bin/bash
set -e

echo "Installing system packages required for Python builds"
# Update package indexes and install common build dependencies
yum -y update
yum -y install gcc make automake autoconf libtool \
    python3-devel openssl-devel libffi-devel \
    postgresql-devel libxml2-devel libxslt-devel

# Ensure pip, setuptools and wheel are up-to-date
python3 -m pip install --upgrade pip setuptools wheel
