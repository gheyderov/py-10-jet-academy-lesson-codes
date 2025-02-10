# Generated by Django 5.1.5 on 2025-02-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='products', to='product.producttag'),
        ),
    ]
