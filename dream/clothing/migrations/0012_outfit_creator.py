# Generated by Django 3.0.6 on 2020-06-08 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clothing', '0011_outfit_favorited_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='outfit',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
