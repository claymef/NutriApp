# nutrisistema/urls.py
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from catalogo.api import router as catalogo_router
from recetas.api import router as recetas_router  # 1. Importas el router

api = NinjaAPI(title="NutriSistema API", version="1.0")

api.add_router("/catalogo/", catalogo_router)
api.add_router("/recetas/", recetas_router)       # 2. Lo registras

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]