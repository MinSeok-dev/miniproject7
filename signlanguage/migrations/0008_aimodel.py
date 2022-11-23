# Generated by Django 3.2 on 2022-11-22 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signlanguage', '0007_delete_aimodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ai_file', models.FileField(blank=True, upload_to='')),
                ('version', models.CharField(max_length=100)),
                ('is_selected', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
