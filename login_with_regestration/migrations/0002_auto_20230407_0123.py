# Generated by Django 2.2.4 on 2023-04-06 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_with_regestration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendship',
            name='users',
        ),
        migrations.AlterUniqueTogether(
            name='likecomment',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='likecomment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='likecomment',
            name='user_who_like',
        ),
        migrations.AlterUniqueTogether(
            name='likepost',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='likepost',
            name='post',
        ),
        migrations.RemoveField(
            model_name='likepost',
            name='user_who_like',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message_receiver',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message_sender',
        ),
        migrations.RemoveField(
            model_name='ourmessage',
            name='user_group1',
        ),
        migrations.RemoveField(
            model_name='ourmessage',
            name='user_group2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user_who_post',
        ),
        migrations.AlterUniqueTogether(
            name='request',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='request',
            name='request_reciever',
        ),
        migrations.RemoveField(
            model_name='request',
            name='request_sender',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='FriendShip',
        ),
        migrations.DeleteModel(
            name='LikeComment',
        ),
        migrations.DeleteModel(
            name='LikePost',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='OurMessage',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Request',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
