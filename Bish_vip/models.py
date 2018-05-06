from xmlrpc.client import DateTime

import os
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.forms import ModelChoiceField
from django.http import request

from comments.models import Comment
from django.urls import reverse


# Create your models here.
def upload_location(instance, filename):
    return os.path.join(settings.BASE_DIR, '/form_{0}/{1}'.format(instance.user.id, filename))


class choises_hair(models.Model):
    value = models.CharField(max_length=30, default="-")

    def __str__(self):
        return self.value


class choiseRaceType(models.Model):
    value = models.CharField(max_length=30, default="-")

    def __str__(self):
        return self.value


class choiseEyeColor(models.Model):
    value = models.CharField(max_length=30, default="-")

    def __str__(self):
        return self.value


class choiseBodyType(models.Model):
    value = models.CharField(max_length=30, default="-")

    def __str__(self):
        return self.value


class Post(models.Model):
    user = models.ForeignKey(get_user_model(), default=1, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=15, null=False, blank=True)
    height = models.CharField(max_length=10, null=False, blank=True)
    grud = models.CharField(max_length=10, null=False, blank=True)
    RaceType = models.ForeignKey(choiseRaceType, default=1, on_delete=models.CASCADE, null=True, blank=True)
    WorkDestrict = models.CharField(max_length=50, null=True, blank=False)
    weight = models.CharField(max_length=10, null=False, blank=True)
    eyeColor = models.ForeignKey(choiseEyeColor, default=1, on_delete=models.CASCADE, null=False, blank=True)
    hair = models.ForeignKey(choises_hair, default=1, on_delete=models.CASCADE, null=False, blank=True)
    BodyType = models.ForeignKey(choiseBodyType, default=1, on_delete=models.CASCADE, null=False, blank=True)
    Description = models.TextField(null=False, blank=True)
    phone = models.CharField(max_length=15, null=False, blank=True)
    image_1 = models.FileField(null=False, blank=True)
    image_2 = models.FileField(upload_to=upload_location, null=True, blank=True)
    image_3 = models.FileField(upload_to=upload_location, null=True, blank=True)
    image_4 = models.FileField(upload_to=upload_location, null=True, blank=True)
    image_5 = models.FileField(upload_to=upload_location, null=True, blank=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    appart_1 = models.CharField(max_length=10, default="-", blank=True)
    appart_2 = models.CharField(max_length=10, default="-", blank=True)
    appart_naigth = models.CharField(max_length=10, default="-", blank=True)
    outside_1 = models.CharField(max_length=10, default="-", blank=True)
    outside_2 = models.CharField(max_length=10, default="-", blank=True)
    outside_nigth = models.CharField(max_length=10, default="-", blank=True)

    main_classic = models.BooleanField(default=False)
    main_blowJob_w_condom = models.BooleanField(default=False)
    main_cunni = models.BooleanField(default=False)
    main_group_sex = models.BooleanField(default=False)
    main_lesbi_lesbi = models.BooleanField(default=False)

    mbr = models.BooleanField(default=False)
    mbr_price = models.TextField(max_length=10, null=True, blank=True)
    anal_sex = models.BooleanField(default=False)
    anal_sex_price = models.TextField(max_length=10, null=True, blank=True)

    dop_end_mouth = models.BooleanField(default=False)
    dop_end_face = models.BooleanField(default=False)
    dop_glub_minet = models.BooleanField(default=False)
    dop_toys = models.BooleanField(default=False)
    dop_role_game = models.BooleanField(default=False)
    dop_couple_service = models.BooleanField(default=False)
    dop_video = models.BooleanField(default=False)
    dop_company = models.BooleanField(default=False)

    massage_relax = models.BooleanField(default=False)
    massage_classic = models.BooleanField(default=False)
    massage_profi = models.BooleanField(default=False)
    massage_tiski = models.BooleanField(default=False)
    massage_prostat = models.BooleanField(default=False)
    massage_erotic = models.BooleanField(default=False)
    massage_sakura = models.BooleanField(default=False)

    dance_profi = models.BooleanField(default=False)
    dance_NoProfi = models.BooleanField(default=False)
    dance_lesbi_show = models.BooleanField(default=False)
    dance_lisbi = models.BooleanField(default=False)

    sado_bandaj = models.BooleanField(default=False)
    sado_gospoja = models.BooleanField(default=False)
    sado_rabyn = models.BooleanField(default=False)
    sado_dominant = models.BooleanField(default=False)
    sado_porka = models.BooleanField(default=False)
    sado_fetish = models.BooleanField(default=False)
    sado_trampling = models.BooleanField(default=False)

    extrim_anilingus = models.BooleanField(default=False)
    extrim_dojd_out = models.BooleanField(default=False)
    extrim_dojd_in = models.BooleanField(default=False)
    extrim_strapon = models.BooleanField(default=False)
    extrim_fisting_anal = models.BooleanField(default=False)
    extrim_fisting_vagin = models.BooleanField(default=False)

    user_is_active = models.BooleanField(default=True)
    admin_is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.Name

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    class MyModelChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "#%i" % obj.id
