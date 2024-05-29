# Generated by Django 4.2.9 on 2024-05-23 19:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import reservations.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_payment'),
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='party_size',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='reservation_date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='special_requests',
        ),
        migrations.RemoveField(
            model_name='table',
            name='table_number',
        ),
        migrations.AddField(
            model_name='reservation',
            name='end_time',
            field=models.DateTimeField(default=reservations.models.default_end_time),
        ),
        migrations.AddField(
            model_name='reservation',
            name='expires_at',
            field=models.DateTimeField(default=reservations.models.default_end_time),
        ),
        migrations.AddField(
            model_name='reservation',
            name='order',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.order'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reserved_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reservation',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='table',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='table',
            name='number',
            field=models.IntegerField(default=1, unique=True),
        ),
    ]