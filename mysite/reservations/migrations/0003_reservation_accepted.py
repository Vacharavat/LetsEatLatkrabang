# Generated by Django 3.0.5 on 2020-04-28 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20200427_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='reservation_accepted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reser_status', models.CharField(choices=[('Accepted', 'accepted'), ('Rejected', 'rejected'), ('Pending', 'pending')], max_length=8)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.myreservation')),
            ],
        ),
    ]
