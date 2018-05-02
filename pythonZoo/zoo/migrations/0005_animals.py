# Generated by Django 2.0.4 on 2018-04-30 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0004_auto_20180426_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Animal Name', max_length=200)),
                ('parentExhibit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parentExhibit', to='zoo.Exhibit')),
            ],
        ),
    ]
