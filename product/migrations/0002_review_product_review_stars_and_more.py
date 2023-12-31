# Generated by Django 4.2.7 on 2023-11-23 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='product.product'),
        ),
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='описание ПРОДУКТА'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='название ПРОДУКТА'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
