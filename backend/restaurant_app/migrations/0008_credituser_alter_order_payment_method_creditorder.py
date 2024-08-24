# Generated by Django 5.1 on 2024-08-24 05:29

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0007_alter_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('last_payment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_due', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Cash'), ('bank', 'Bank'), ('cash-bank', 'Cash and Bank'), ('credit', 'Credit')], default='cash', max_length=20),
        ),
        migrations.CreateModel(
            name='CreditOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restaurant_app.order')),
                ('credit_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_orders', to='restaurant_app.credituser')),
            ],
        ),
    ]
