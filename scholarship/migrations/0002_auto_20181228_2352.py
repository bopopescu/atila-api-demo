# Generated by Django 2.1.4 on 2018-12-28 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('helpers', '0001_initial'),
        ('userprofile', '0001_initial'),
        ('scholarship', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='applicants',
            field=models.ManyToManyField(related_name='scholarship_applicants', through='scholarship.Application', to='userprofile.UserProfile'),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='city',
            field=models.ManyToManyField(blank=True, to='helpers.City'),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='country',
            field=models.ManyToManyField(blank=True, to='helpers.Country'),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scholarship_owner', to='userprofile.UserProfile'),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='province',
            field=models.ManyToManyField(blank=True, to='helpers.Province'),
        ),
        migrations.AddField(
            model_name='application',
            name='scholarship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholarship.Scholarship'),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.UserProfile'),
        ),
    ]
