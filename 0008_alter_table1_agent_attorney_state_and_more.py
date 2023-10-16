# Generated by Django 4.2.6 on 2023-10-15 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_alter_table1_employer_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table1',
            name='AGENT_ATTORNEY_STATE',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='CASE_STATUS',
            field=models.CharField(choices=[('CERTIFIED-WITHDRAWN', 'CERTIFIED-WITHDRAWN'), ('WITHDRAWN', 'WITHDRAWN'), ('CERTIFIED', 'CERTIFIED'), ('DENIED', 'DENIED')], max_length=190, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='CASE_SUBMITTED',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='DECISION_DATE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='EMPLOYER_PHONE',
            field=models.CharField(max_length=130, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='EMPLOYER_PHONE_EXT',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='EMPLOYER_STATE',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='EMPLOYMENT_END_DATE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='EMPLOYMENT_START_DATE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='H_1B_DEPENDENT',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='NAIC_CODE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='ORIGINAL_CERT_DATE',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='PREVAILING_WAGE',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='PW_WAGE_SOURCE',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='SOC_CODE',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='SOC_NAME',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='TOTAL_WORKERS',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='WAGE_RATE_OF_PAY_FROM',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='WAGE_RATE_OF_PAY_TO',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='WILLFUL_VIOLATOR',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]