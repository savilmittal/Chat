# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-04-02 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20160825_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='privatekey',
            field=models.TextField(default='-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQC9EOI/GpCKmWwuSZO6ga0bt/dzHyP3+RErOkVozB+CQd70M/2R5593S2K1NAtid2jok1GV39DhlvGQYicwrM+RC7m39crXypmMzU+ERPGLJszRlmnL\nMtOdEIn7xGjVREu0dNomW343rZ/Asd2HowHd8leio4sjivLkQZZkIKzbPwIDAQAB\nAoGBAJCaskCLg9POBnTcp5W1iv4xVZyCS9NkdyI13lKKFOtekDT88ss+ebQXP3bS\nSIbWR7Hiwzq7RZrVBQtmVw0ej13QNGdwk0B3uZ0VxcSW8vGOC19DZIR+dY/ucMuv\nIzdhNlHq0AL1hNsMevgoZTOOlFutf1xQkz0egB4nbTb/6OeZAkEAwKGBLV7Wk2ST\n9gU8CDlr56vOuMXnZznu8uillDj/jQavsxv2mHkKor3gljOxkIpnJn0S7sSDCW7O\nveITR02PbQJBAPtDKEyEVIzr0naYf2GkTF56PkD+Bycd0+jEQ69gu+LtgWiJBsyR\nC3iQrWlsnwW8GUyHv6CtFQiq3CMVd/BxLdsCQAXepf4I7sbtAKk1fZ/OiCA2FwWA\nWk3F8ScLucfreLYGZyIxDvGUdqOA37AUASwjW4NLumD2Mfv+mWQl2GqKzX0CQQDf\nfFh31qwtvAOzIOkMPEsBLdH5lPlfvZQi0Y8yiuQTcBVOmbLGeayuTGEyCD9ZpnkK\nLSQxEkJHN1IekpXf84tJAkBXHLnHc8EFxJtY2j6iPgsaMz2oNOcS+0jvR7kHsdC7\nPKcSc2BDwdN8SSvdRTFA6J6td7afmhdqXa7kIbKRXdGR\n-----END RSA PRIVATE KEY-----', max_length=1000),
        ),
        migrations.AddField(
            model_name='myuser',
            name='publickey',
            field=models.TextField(default='-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9EOI/GpCKmWwuSZO6ga0bt/dz\nHyP3+RErOkVozB+CQd70M/2R5593S2K1NAtid2jok1GV39DhlvGQYicwrM+RC7m3\n9crXypmMzU+ERPGLJszRlmnLMtOdEIn7xGjVREu0dNomW343rZ/Asd2HowHd8lei\no4sjivLkQZZkIKzbPwIDAQAB\n-----END PUBLIC KEY-----', max_length=1000),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profilepic',
            field=models.ImageField(default='static/default/anonymous.jpg', upload_to='static/profilepics/', verbose_name='Profile Pic'),
        ),
    ]
