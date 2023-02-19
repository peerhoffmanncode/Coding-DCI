import os

#####################################################################
### SETTINGS                                                        #
#####################################################################
# Django Secrets
os.environ[
    "SECRET_KEY"
] = "django-insecure-%syvyzq4@1aqqs+0y9%2olp&vr3kfi^50eg=ngx^b*xyfh+-hm"

#####################################################################
### DATABASE                                                        #
#####################################################################

# Postgres authentication locally
# os.environ["DB_NAME"] = "hotsox_db"
# os.environ["DB_USER"] = "postgres"
# os.environ["DB_PASSWORD"] = "postgres"
# os.environ["DB_HOST"] = "localhost"
# os.environ["DB_PORT"] = "5432"

# Postgres remote authentication https://elephantsql.com
os.environ["DB_NAME"] = "fjiyvlda"
os.environ["DB_USER"] = "fjiyvlda"
os.environ["DB_PASSWORD"] = "U0CBx-jidiaB1FyZlw3K7Y9NMc5oWUwo"
os.environ["DB_HOST"] = "dumbo.db.elephantsql.com"
os.environ["DB_PORT"] = "5432"

#####################################################################
### APIs                                                            #
#####################################################################
# Google OAuth
os.environ[
    "GOOGLE_CLIENT_ID"
] = "280227823700-hm0qg17uub44b0nbfhhja1pmugi58hct.apps.googleusercontent.com"
os.environ["GOOGLE_SECRET"] = "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"

# Cloudinary
os.environ[
    "CLOUDINARY_URL"
] = "cloudinary://122629547437485:wNGghdoP_Uv3JIQ22ix0oWr-8hc@ddvfqbtpr"
os.environ["cloudinary_cloud_name"] = "ddvfqbtpr"
os.environ["cloudinary_api_key"] = "122629547437485"
os.environ["cloudinary_api_secret"] = "wNGghdoP_Uv3JIQ22ix0oWr-8hc"
