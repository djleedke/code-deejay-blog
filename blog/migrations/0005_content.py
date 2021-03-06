# Generated by Django 3.0.6 on 2020-06-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('content', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
