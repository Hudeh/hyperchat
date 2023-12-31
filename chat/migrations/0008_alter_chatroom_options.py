# Generated by Django 5.0 on 2023-12-12 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0007_alter_chatroom_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="chatroom",
            options={
                "ordering": ("-created_at",),
                "permissions": [
                    ("custom_chat_room_delete", "Can delete chat room"),
                    ("custom_chat_room_add", "Can add chat room"),
                    ("custom_chat_room_view", "Can view chat room"),
                    ("custom_chat_room_edit", "Can edit chat room"),
                ],
            },
        ),
    ]
