# Generated by Django 5.0.6 on 2024-06-07 08:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StreamPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=150)),
                ('website', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('storyline', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='watchlist_app.streamplatform')),
            ],
        ),
    ]
