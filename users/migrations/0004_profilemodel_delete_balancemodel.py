# Generated by Django 4.2.7 on 2024-02-11 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('borrowed_books', models.ManyToManyField(to='books.book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='BalanceModel',
        ),
    ]