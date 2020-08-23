# Generated by Django 3.0.7 on 2020-08-22 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itrac', '0018_auto_20200820_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]