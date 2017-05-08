#!/bin/bash

pushd /home/tietopyynto/tietopyynto
source /home/tietopyynto/env/bin/activate
export DJANGO_SETTINGS_MODULE="froide.custom_settings"
export DJANGO_CONFIGURATION="TietopyyntoProd"

celery worker -B -Q celery,emailfetch -l INFO --pidfile=celeryd.pid -A froide --detach
popd
