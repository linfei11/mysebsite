# Generated by Django 3.2.3 on 2021-05-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_attack_rule_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attack',
            name='rule_name',
            field=models.CharField(max_length=300, null=True, verbose_name='规则名'),
        ),
    ]
