# Generated by Django 2.0 on 2018-01-08 22:21

import datetime

import django.db.models.deletion
from django.db import migrations, models

ADMIN = 2


def make_owner_admin(apps, schema_editor):
    Team = apps.get_model("events", "Team")
    Member = apps.get_model("events", "Member")
    for team in Team.objects.all():
        Member.objects.get_or_create(
            team=team,
            user=team.owner_profile,
            role=ADMIN,
            joined_date=team.created_date or datetime.datetime.now(),
        )


class Migration(migrations.Migration):

    dependencies = [("events", "0004_auto_20180103_2212")]

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "role",
                    models.SmallIntegerField(
                        choices=[(0, "Normal"), (1, "Moderator"), (2, "Administrator")],
                        db_index=True,
                        default=0,
                        verbose_name="Member Role",
                    ),
                ),
                ("joined_date", models.DateTimeField(default=datetime.datetime.now)),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.Team"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.UserProfile",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="team",
            name="members",
            field=models.ManyToManyField(
                blank=True,
                related_name="memberships",
                through="events.Member",
                to="events.UserProfile",
            ),
        ),
        migrations.RunPython(make_owner_admin),
    ]
