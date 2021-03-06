# Generated by Django 2.2.17 on 2021-01-31 00:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.CharField(max_length=100, verbose_name='部位')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='イメージ画像')),
                ('cause', models.TextField(verbose_name='原因')),
                ('improve', models.TextField(verbose_name='対策')),
                ('video', models.CharField(blank=True, max_length=200, null=True, verbose_name='動画')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
    ]
