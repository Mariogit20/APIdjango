"""
URL configuration for crud_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

####### A] Si dans l'     URL      DU NAVIGATEUR       MOZILLA FIREFOX      , on saisit :                http://127.0.0.1:8000/
# APPLICATION   produits
# MODELE        produits
# http://127.0.0.1:8000/produits/

#    path('api/',include('produits.urls'))

# # ALORS ON OBTIENT :
#      Api Root Produit List 

# Produit List

# GET /produits/

# HTTP 200 OK
# Allow: GET, POST, HEAD, OPTIONS
# Content-Type: application/json
# Vary: Accept

# [
#     {
#         "id": 1,
#         "nom": "RealMe",
#         "description": "120go - 8 go ram",
#         "prix": "3000000.00",
#         "image": "http://127.0.0.1:8000/static/image/produits/stock-vector-186615066-m-2015.jpg",
#         "date_ajout": "2025-10-18T16:05:22.901175Z"
#     },
#     {
#         "id": 2,
#         "nom": "Iphone",
#         "description": "sdfghjkl",
#         "prix": "3000000.00",
#         "image": "http://127.0.0.1:8000/static/image/produits/arrangement-black-friday-shopping-carts-with-copy-space_23-2148667047.jpg",
#         "date_ajout": "2025-10-18T17:40:49.735111Z"
#     }
# ]





####### B] Si dans l'     URL      DU NAVIGATEUR       MOZILLA FIREFOX      , on saisit :                http://127.0.0.1:8000/
# APPLICATION   contact
# MODELE        contact
# http://127.0.0.1:8000/contact/

#    path('api/',include('contact.urls'))

# # ALORS ON OBTIENT :
#      Api Root Contact List 

# Contact List

# GET /contact/

# HTTP 200 OK
# Allow: GET, POST, HEAD, OPTIONS
# Content-Type: application/json
# Vary: Accept

# [
#     {
#         "id": 1,
#         "nom": "RAKOTO",
#         "email": "ra@yahoo.fr",
#         "message": "salut rakoto",
#         "date_envoi": "2025-10-25T12:49:08.207376Z"
#     },
#     {
#         "id": 2,
#         "nom": "RAZANAKOLONA",
#         "email": "Edgard@hotmail.fr",
#         "message": "Préparation du repas d'Edgard d'Assisé !",
#         "date_envoi": "2025-10-25T12:54:43.961650Z"
#     }
# ]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('produits.urls')),       #    path('api/',include('produits.urls'))
    path('',include('contact.urls')),
    path('',include('sliders.urls'))    
]

