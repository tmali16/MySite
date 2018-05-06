from django.contrib import admin

from Bish_vip.models import *


# Register your models here.


class PostModelAdmin(admin.AdminSite):
    class Meta:
        model = Post


admin.site.register(Post)

admin.site.register(choiseBodyType)
admin.site.register(choiseEyeColor)
admin.site.register(choiseRaceType)
admin.site.register(choises_hair)