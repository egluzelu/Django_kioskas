# Generated by Django 5.0 on 2024-02-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_options_blog_created_at_blog_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-updated_at'], 'verbose_name': 'blog', 'verbose_name_plural': 'blogs'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='name of the blog'),
        ),
    ]
