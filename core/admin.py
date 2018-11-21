from django.contrib import admin

from core.models import Person, Address, PhoneNumber, Organization
# Register your models here.


admin.site.register(Person)
admin.site.register(Address)
admin.site.register(PhoneNumber)
admin.site.register(Organization)
