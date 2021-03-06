# Generated by Django 2.2.4 on 2020-03-21 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('title', models.CharField(blank=True, max_length=50)),
                ('video', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('professor', models.CharField(blank=True, max_length=20)),
                ('opendate', models.CharField(blank=True, max_length=8)),
                ('closedate', models.CharField(blank=True, max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=99)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('note', models.TextField(blank=True, max_length=500)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('title', models.CharField(blank=True, max_length=50)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.ClassRoom')),
            ],
        ),
        migrations.CreateModel(
            name='LectureImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=99)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.Lecture')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='weeklyclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.WeeklyClass'),
        ),
    ]
