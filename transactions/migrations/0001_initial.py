# Generated by Django 4.2.7 on 2024-02-11 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0002_alter_book_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_book', models.BooleanField(default=False)),
                ('returned_book', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
