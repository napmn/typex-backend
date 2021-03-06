# Generated by Django 3.1.2 on 2020-10-08 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('quote_type', models.CharField(choices=[('KNOWN', 'Known')], max_length=30, verbose_name='type')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quotes.author')),
            ],
            options={
                'verbose_name': 'quote',
                'verbose_name_plural': 'quotes',
            },
        ),
    ]
