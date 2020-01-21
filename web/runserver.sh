#!/bin/bash

gunicorn --log-level info --log-file=- --workers 1 --name app -b 0.0.0.0:8000 --reload app.app:app 
