from functools import wraps
from flask import request, redirect, url_for, abort
from data import ALL_BRANDS
from hasweb import app


def get_brand(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        request_host = request.environ['HTTP_HOST']
        if request_host is not None:
            if ':' in request_host:
                request_host = request_host.split(':', 1)[0]

            temp_brand = None # If we don't find a brand
            temp_brand_key = None
            for brand_key, brand in ALL_BRANDS.iteritems():
                if app.debug:
                    if brand['hostname'][:brand['hostname'].rindex('.')] in request_host: # allow rootconf.dev style domains when in development
                        temp_brand = brand
                        temp_brand_key = brand_key
                else:
                    if brand['hostname'] == request_host:
                        temp_brand = brand
                        temp_brand_key = brand_key

            if temp_brand is None:
                abort(404)
            else:
                return f(brand=temp_brand, brand_id=temp_brand_key, *args, **kwargs)
        else:
            abort(404)

    return decorated_function
