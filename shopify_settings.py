# Replace the API Key and Shared Secret with the one given for your
# App by Shopify.
#
# To create an application, or find the API Key and Secret, visit:
# - for private Apps:
#     https://${YOUR_SHOP_NAME}.myshopify.com/admin/api
# - for partner Apps:
#     https://www.shopify.com/services/partners/api_clients
#
# You can ignore this file in git using the following command:
#   git update-index --assume-unchanged shopify_settings.py
SHOPIFY_API_KEY = 'some_key'
SHOPIFY_API_SECRET = 'some_secret'

# See http://api.shopify.com/authentication.html for available scopes
# to determine the permissions your app will need.
SHOPIFY_API_SCOPE = ['read_products', 'read_orders']
