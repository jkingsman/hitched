#!/usr/bin/env bash

NAME="core.wsgi.application"                                  # Name of the application
DJANGODIR=/home/ubuntu/hitched/app             # Django project directory
SOCKFILE=/home/ubuntu/hitched/gunicorn.sock  # we will communicte using this unix socket
USER=ubuntu                                        # the user to run as
GROUP=ubuntu                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=settings_prod           # which settings file should Django use
DJANGO_WSGI_MODULE=core.wsgi.application                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
