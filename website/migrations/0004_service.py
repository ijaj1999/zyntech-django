# Generated by Django 5.1.1 on 2025-03-20 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_blogpost_image_blogpost_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('short_description', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='services/')),
                ('icon', models.CharField(help_text="Use Bootstrap icons (e.g., 'bi bi-code-slash')", max_length=100)),
            ],
        ),
    ]
