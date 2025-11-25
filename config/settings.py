import os
from pathlib import Path

import environ
from oscar.defaults import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- django-environ setup ---
env = environ.Env(
    # Set default values for variables and cast their types
    DEBUG=(bool, False)
)
# Read the .env file
# This is a crucial step that was missing. It loads variables from the .env file.
environ.Env.read_env(env_file=str(BASE_DIR / ".env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

# Use env.list() to correctly parse a comma-separated string
# from the .env file into a list.
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["127.0.0.1"])


# Conditional settings based on DEBUG
if not DEBUG:
    # === Security Settings for Production ===
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"

LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "index"

ACCOUNT_LOGIN_METHODS = {"username", "email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "username*", "password1*", "password2*"]
ACCOUNT_EMAIL_VERIFICATION = "optional"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Allow unauthenticated access to these paths; everything else requires login
LOGIN_REQUIRED_EXEMPT_URLS = [
    r"^accounts/.*",  # allauth: login, signup, password reset,
    # email confirm, social callbacks
    r"^admin/login/$",  # allow admin login
    r"^static/.*",  # static assets
    r"^media/.*",  # media files (if served by Django)
    r"^api/.*",  # let DRF permission classes handle API auth
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.flatpages",
    "django.contrib.sites",
    # Third party apps
    "rest_framework",
    "ninja",
    "django_htmx",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "waffle",
    "oscar.config.Shop",
    "oscar.apps.analytics.apps.AnalyticsConfig",
    "oscar.apps.checkout.apps.CheckoutConfig",
    "oscar.apps.address.apps.AddressConfig",
    "oscar.apps.shipping.apps.ShippingConfig",
    "oscar.apps.catalogue.apps.CatalogueConfig",
    "oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig",
    "oscar.apps.communication.apps.CommunicationConfig",
    "oscar.apps.partner.apps.PartnerConfig",
    "oscar.apps.basket.apps.BasketConfig",
    "oscar.apps.payment.apps.PaymentConfig",
    "oscar.apps.offer.apps.OfferConfig",
    "oscar.apps.order.apps.OrderConfig",
    "oscar.apps.customer.apps.CustomerConfig",
    "oscar.apps.search.apps.SearchConfig",
    "oscar.apps.voucher.apps.VoucherConfig",
    "oscar.apps.wishlists.apps.WishlistsConfig",
    "oscar.apps.dashboard.apps.DashboardConfig",
    "oscar.apps.dashboard.reports.apps.ReportsDashboardConfig",
    "oscar.apps.dashboard.users.apps.UsersDashboardConfig",
    "oscar.apps.dashboard.orders.apps.OrdersDashboardConfig",
    "oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig",
    "oscar.apps.dashboard.offers.apps.OffersDashboardConfig",
    "oscar.apps.dashboard.partners.apps.PartnersDashboardConfig",
    "oscar.apps.dashboard.pages.apps.PagesDashboardConfig",
    "oscar.apps.dashboard.ranges.apps.RangesDashboardConfig",
    "oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig",
    "oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig",
    "oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig",
    "oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig",
    "crm",
    "django_celery_results",
    "widget_tweaks",
    "haystack",
    "treebeard",
    "sorl.thumbnail",
    "django_tables2",
    # Apps
    "landing",
    "store.apps.StoreConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "oscar.apps.basket.middleware.BasketMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]

if DEBUG:
    INSTALLED_APPS += [
        "debug_toolbar",
    ]

    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

    # This setting is REQUIRED for the toolbar to appear in the browser
    INTERNAL_IPS = [
        "127.0.0.1",
    ]

# DRF: default to authenticated; public endpoints can override with AllowAny
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "oscar.apps.search.context_processors.search_form",
                "oscar.apps.checkout.context_processors.checkout",
                "oscar.apps.communication.notifications.context_processors.notifications",
                "oscar.core.context_processors.metadata",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "landing.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {"default": env.db()}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Django Oscar Settings (Minimum Requirements)
OSCAR_SHOP_NAME = "P2's Spice Company"
OSCAR_FROM_EMAIL = "support@p2spice.com"
OSCAR_DEFAULT_CURRENCY = "USD"
SITE_ID = 1  # Required by Allauth and Oscar

# Optional: Set the user model if Oscar doesn't find it automatically
OSCAR_USER_MODEL = "auth.User"

WHOOSH_INDEX_PATH = os.path.join(BASE_DIR, "whoosh_index")

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": WHOOSH_INDEX_PATH,
    },
}


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static and Media files
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATIC_ROOT = BASE_DIR / "staticfiles_collected"
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Session-based cart settings
CART_SESSION_ID = "cart"

# Stripe API keys
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")
STRIPE_PUBLIC_KEY = env("STRIPE_PUBLIC_KEY")
