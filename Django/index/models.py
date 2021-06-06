from django.db import models

# Create your models here.
class Attack(models.Model):
    # risk_level
    NO_RISK = 0
    NORMAL_RISK = 1
    ATTENTION_RISK = 2
    SERIOUS_RISK = 3
    URGENT_RISK = 4
    RISK_LEVEL = (
        (NO_RISK, '无风险'),
        (NORMAL_RISK, '一般'),
        (ATTENTION_RISK, '关注'),
        (SERIOUS_RISK, '严重'),
        (URGENT_RISK, '紧急'),
    )
    # input_type
    BATCH_INPUT = 1
    MANUAL_INPUT = 2
    AUTO_INPUT = 3
    INPUT_TYPE = (
        (BATCH_INPUT, '批量导入'),
        (MANUAL_INPUT, '手动添加'),
        (AUTO_INPUT, '自动收集'),
    )
    insert_time = models.DateTimeField(auto_now_add=True, verbose_name='插入时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    user = models.CharField(max_length=50, verbose_name='规则添加者')
    risk_level = models.PositiveIntegerField(default=NO_RISK, choices=RISK_LEVEL, verbose_name='规则等级')
    input_type = models.PositiveIntegerField(default=MANUAL_INPUT, choices=INPUT_TYPE, verbose_name='导入类型')
    rule_id = models.CharField(max_length=100, verbose_name='规则id')
    rule_type = models.CharField(max_length=50, verbose_name='规则类型')
    
    rule_name = models.CharField(max_length=300, null=True, blank=True, verbose_name='规则名')
    content = models.CharField(max_length=1000, verbose_name='规则内容')
    pcap_path = models.FileField(upload_to=r'uploads/', null=True, blank=True, verbose_name='验证规则的pcap文件')
    comment = models.CharField(max_length=1000, null=True, blank=True, verbose_name='用户评论')

    class Meta:
        db_table = 'attacks'
        verbose_name = 'attacks'
        verbose_name = verbose_name_plural = 'Attacks'

    def __str__(self):
        return self.rule_name