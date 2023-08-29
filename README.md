# ecommerce
E-commerce API

docker-compose exec web python manage.py createsuperuser

celery -A config  worker -l info --pool=solo 
docker-compose 

docker-compose run web python3 manage.py createsuperuser


NEW CHANGES
✅ Refactoring  according to best practises
✅ Added dotenv for security
✅ Custom Permissions
✅ Order Products
✅ replenish and reduce stock of products
✅ Django signals, integration to telegram bot




## Dumdata from old server: 
python manage.py dumpdata > data.json


## Cleaning database in new server:
python manage.py flush 

## Load data in new server:
python manage.py loaddata data.json

