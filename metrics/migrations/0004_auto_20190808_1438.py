# Generated by Django 2.1.7 on 2019-08-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("metrics", "0003_auto_20190605_0927")]

    operations = [
        migrations.CreateModel(
            name="MetricLead",
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
                ("name", models.TextField(unique=True)),
            ],
            options={"ordering": ["name"], "abstract": False},
        ),
        migrations.CreateModel(
            name="TeamLead",
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
                ("name", models.TextField(unique=True)),
            ],
            options={"ordering": ["name"], "abstract": False},
        ),
        migrations.CreateModel(
            name="Topic",
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
                ("name", models.TextField(unique=True)),
            ],
            options={"ordering": ["name"], "abstract": False},
        ),
        migrations.AlterModelOptions(
            name="organisation", options={"ordering": ["name"]}
        ),
        migrations.AlterModelOptions(name="report", options={"ordering": ["name"]}),
        migrations.RemoveField(model_name="metric", name="metric_lead"),
        migrations.RemoveField(model_name="metric", name="team_lead"),
        migrations.RemoveField(model_name="metric", name="theme"),
        migrations.AddField(
            model_name="metric",
            name="display_name",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="metric",
            name="indicator_type",
            field=models.TextField(
                choices=[
                    ("Process", "Process"),
                    ("Structure", "Structure"),
                    ("Outcome", "Outcome"),
                ],
                default="",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="metric",
            name="upstream_id",
            field=models.TextField(default="", verbose_name="Metric ID"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="organisation", name="name", field=models.TextField(unique=True)
        ),
        migrations.AlterField(
            model_name="report", name="name", field=models.TextField(unique=True)
        ),
        migrations.DeleteModel(name="Lead"),
        migrations.DeleteModel(name="Team"),
        migrations.DeleteModel(name="Theme"),
        migrations.AddField(
            model_name="metric",
            name="topics",
            field=models.ManyToManyField(to="metrics.Topic"),
        ),
    ]
