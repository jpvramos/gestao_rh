# Generated by Django 3.2.5 on 2021-07-18 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_alter_funcionario_user'),
        ('documentos', '0002_documento_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='funcionario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario'),
            preserve_default=False,
        ),
    ]
