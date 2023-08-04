#!/bin/bash

docker run -it --name higher-lower -v $(pwd)/app:/app -w /app python:latest bash
