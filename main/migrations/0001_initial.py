# Generated by Django 4.2.4 on 2023-10-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_key', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=255)),
                ('rating', models.FloatField(default=0)),
                ('image_link', models.URLField(default='https://img.freepik.com/premium-vector/open-blank-book-illustration-school-supply-back-school-open-book-icon-reading-writing_502505-530.jpg?w=2000', max_length=300)),
            ],
        ),
    ]
