# rssassin-feed
Converts websites I want to read to RSS

## To add new feed
```sh 
docker-compose run python manage.py startapp YOUR_SITE
```

where YOUR_SITE is the new feed you want to add.

Add `YOUR_SITE/urls.py` to `rssasin_feed/urls.py` 

Add logic to parse site and expose RSS to `YOUR_SITE/views.py`