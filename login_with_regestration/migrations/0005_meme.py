# Generated by Django 2.2.4 on 2023-04-12 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_with_regestration', '0004_auto_20230411_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meme_content', models.TextField()),
                ('meme_caption', models.TextField()),
                ('status_code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]