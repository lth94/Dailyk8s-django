# Generated by Django 4.1.1 on 2022-12-23 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('userstat', '0003_alter_solved_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solved',
            name='problem_id',
            field=models.ForeignKey(db_column='pk', on_delete=django.db.models.deletion.CASCADE, to='main.problem'),
        ),
    ]