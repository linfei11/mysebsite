# Generated by Django 3.2.3 on 2021-06-04 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_alter_attack_risk_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attack',
            name='pcap_path',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='验证规则的pcap文件'),
        ),
        migrations.AlterField(
            model_name='attack',
            name='risk_level',
            field=models.PositiveIntegerField(choices=[(0, '无风险'), (1, '一般'), (2, '关注'), (3, '严重'), (4, '紧急')], default=0, verbose_name='规则等级'),
        ),
    ]
