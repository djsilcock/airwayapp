from website import create_app

app = create_app()

#  Uncomment to use the middleware
#flaskbb.wsgi_app = ReverseProxyPathFix(flaskbb.wsgi_app)

