# Generated by Django 4.0.3 on 2022-07-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('okazje_app', '0004_item_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoToData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_identifier', models.CharField(max_length=200)),
                ('redirection_link', models.URLField()),
            ],
        ),
    ]
