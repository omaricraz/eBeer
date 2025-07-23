from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('ebeer_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('image', models.ImageField(upload_to='products/')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
