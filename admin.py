from django.contrib import admin

# Register your models here.
from django.contrib import admin  
    
# Register your models here.  
from .models import GeeksModel  
from .models import DataApi
from .models import student
from .models import emp
    
admin.site.register(GeeksModel)
admin.site.register(DataApi)
admin.site.register(student)
admin.site.register(emp)
