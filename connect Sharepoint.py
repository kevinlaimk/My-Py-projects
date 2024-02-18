from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

site_url = 'https://your_sharepoint_site_url'
username = 'your_username'
password = 'your_password'

context_auth = AuthenticationContext(site_url)
if context_auth.acquire_token_for_user(username, password):
    ctx = ClientContext(site_url, context_auth)
    web = ctx.web
    ctx.load(web)
    ctx.execute_query()
    print(f'Connected to the site: {web.properties["Title"]}')
else:
    print(context_auth.get_last_error())
