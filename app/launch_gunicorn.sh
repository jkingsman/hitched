#!/bin/bash

NAME="hitched"                              #Name of the application (*)
DJANGODIR=/srv/hitched/app          # Django project directory (*)
SOCKFILE=/srv/hitched/app/gunicornsock        # we will communicate using this unix socket (*)
USER=ec2-user                                        # the user to run as (*)
GROUP=ec2-user                                   # the group to run as (*)
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=core.settings_prod         # which settings file should Django use (*)
DJANGO_WSGI_MODULE=core.wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /usr/local/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE
