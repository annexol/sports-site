# Generated by Django 4.0 on 2022-01-17 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='slug_news',
        ),
        migrations.RemoveField(
            model_name='headnews',
            name='comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='head_news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_head', to='news.headnews', verbose_name='HeadNews'),
        ),
        migrations.AddField(
            model_name='comments',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_news', to='news.news', verbose_name='News'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.newuser', verbose_name='NewUser'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='img/users/'),
        ),
    ]
