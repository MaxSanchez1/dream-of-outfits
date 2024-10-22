# Generated by Django 3.0.6 on 2020-06-05 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0008_auto_20200605_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='type',
            new_name='clothing_type',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='texture',
            new_name='material',
        ),
        migrations.RemoveField(
            model_name='article',
            name='brand_example',
        ),
        migrations.RemoveField(
            model_name='article',
            name='cost_of_example',
        ),
        migrations.RemoveField(
            model_name='article',
            name='link_example',
        ),
        migrations.RemoveField(
            model_name='outfit',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='outfit',
            name='description',
        ),
        migrations.RemoveField(
            model_name='outfit',
            name='hat',
        ),
        migrations.RemoveField(
            model_name='outfit',
            name='jacket',
        ),
        migrations.RemoveField(
            model_name='outfit',
            name='socks',
        ),
        migrations.RemoveField(
            model_name='outfit',
            name='bottom',
        ),
        migrations.AddField(
            model_name='outfit',
            name='bottom',
            field=models.ManyToManyField(related_name='outfit_bottom', to='clothing.Article'),
        ),
        migrations.RemoveField(
            model_name='outfit',
            name='shoes',
        ),
        migrations.AddField(
            model_name='outfit',
            name='shoes',
            field=models.ManyToManyField(related_name='outfit_shoes', to='clothing.Article'),
        ),
        migrations.RemoveField(
            model_name='outfit',
            name='top',
        ),
        migrations.AddField(
            model_name='outfit',
            name='top',
            field=models.ManyToManyField(related_name='outfit_top', to='clothing.Article'),
        ),
    ]
