# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
export DJANGO_SETTINGS_MODULE="core.settings_prod"

gunicorn core.wsgi:application \
  --name hitched \
  --workers 1 \
  --user $USER \
  --bind=unix:/srv/hitched/app/gunicornsock \
  --daemon
