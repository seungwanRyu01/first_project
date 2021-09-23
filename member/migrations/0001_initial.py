# Generated by Django 3.2.6 on 2021-09-05 23:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=64, unique=True, verbose_name='사용자 아이디')),
                ('password', models.CharField(max_length=64, verbose_name='사용자 비밀번호')),
                ('username', models.CharField(max_length=64, verbose_name='사용자 이름')),
                ('useremail', models.EmailField(max_length=64, unique=True, verbose_name='사용자 이메일')),
                ('phoneNumber', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='사용자 전화번호')),
                ('registered', models.DateTimeField(auto_now_add=True, verbose_name='계정 생성시간')),
                ('gender', models.CharField(choices=[('M', '남성(Man)'), ('W', '여성(Woman)')], max_length=1, verbose_name='사용자 성별')),
                ('job', models.CharField(choices=[('W', '직장인(Worker)'), ('A', '선수(Athlete)'), ('S', '학생(Student)'), ('P', '대학원생(Postgrade)'), ('E', '기타(etc)')], max_length=1, verbose_name='사용자 직업')),
                ('exercise_frequency', models.CharField(choices=[('VO', '매우 자주'), ('U', '자주'), ('S', '가끔'), ('H', '거의 안함'), ('N', '안함')], max_length=2, verbose_name='사용자 직업')),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저',
                'db_table': 'User',
            },
        ),
    ]
