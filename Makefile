run:
	@python manage.py runserver
migrate:
	@python manage.py migrate
cleanmigrations:
	for a in $$(ls */migrations/ | grep : | cut -d ":" -f 1); do
	  for b in $$(ls $$a); do
	     echo $$b
	  done
	done
