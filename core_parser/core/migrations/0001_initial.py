# Generated by Django 3.1.2 on 2020-10-28 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SecondaryUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_link', models.CharField(max_length=255)),
                ('main_url', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.mainurl')),
            ],
        ),
    ]