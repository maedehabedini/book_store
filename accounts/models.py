from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username


# با سیگنال ها بعد اینکه کاربر رجیستر کرد پروفایل رو میسازه که
# اطلاعات اضافرو خود کاربر داخل پروفایل ویرایش و اضافه کنه و وقتی کاربر رجیستر میکنه شناخته بشه پروفایلش
def save_profile_user(sender, **kwargs):
    if kwargs['created']:
        profile_user = Profile(user=kwargs['instance'])
        profile_user.save()


post_save.connect(receiver=save_profile_user, sender=User)
