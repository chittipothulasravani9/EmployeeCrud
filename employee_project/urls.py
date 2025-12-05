"""
URL configuration for employee_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
'''from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/',include('employee_register.urls'))
]'''

'''from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage! This is the CRUD operations with Django")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee_register.urls')),
    path('', home),  # This will make the homepage work
]'''

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Welcome to the homepage!</h1>
        <p>This is the CRUD operations with Django.</p>
        <a href="/employee/">Go to Employee Page</a>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee_register.urls')),  # Ensure this is correct
    path('', home),  # Homepage view
]





