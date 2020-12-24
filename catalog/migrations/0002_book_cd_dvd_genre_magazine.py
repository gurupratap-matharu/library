# Generated by Django 3.1.4 on 2020-12-24 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('upc', models.PositiveIntegerField(verbose_name='Universal Product Code')),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('volume', models.SmallIntegerField()),
                ('issue', models.SmallIntegerField()),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='catalog_magazine_related', related_query_name='catalog_magazines', to='catalog.catalog')),
                ('contributors', models.ManyToManyField(to='catalog.ContributorWithType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DVD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('upc', models.PositiveIntegerField(verbose_name='Universal Product Code')),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='catalog_dvd_related', related_query_name='catalog_dvds', to='catalog.catalog')),
                ('contributors', models.ManyToManyField(to='catalog.ContributorWithType')),
                ('genre', models.ManyToManyField(to='catalog.Genre')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('upc', models.PositiveIntegerField(verbose_name='Universal Product Code')),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='catalog_cd_related', related_query_name='catalog_cds', to='catalog.catalog')),
                ('contributors', models.ManyToManyField(to='catalog.ContributorWithType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('upc', models.PositiveIntegerField(verbose_name='Universal Product Code')),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('isbn', models.PositiveIntegerField()),
                ('dds', models.PositiveIntegerField()),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='catalog_book_related', related_query_name='catalog_books', to='catalog.catalog')),
                ('contributors', models.ManyToManyField(to='catalog.ContributorWithType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]