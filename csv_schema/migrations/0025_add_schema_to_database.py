# Generated by Django 2.1.5 on 2019-02-12 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("csv_schema", "0024_remove_tables_unique_together")]

    operations = [
        migrations.CreateModel(
            name="Schema",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.TextField()),
                (
                    "database",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schemas",
                        to="csv_schema.Database",
                    ),
                ),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.AddField(
            model_name="table",
            name="schema",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tables",
                to="csv_schema.Schema",
            ),
            preserve_default=False,
        ),
        migrations.RemoveField(model_name="table", name="database"),
        migrations.AlterUniqueTogether(
            name="table", unique_together={("name", "schema")}
        ),
        migrations.AlterUniqueTogether(
            name="schema", unique_together={("name", "database")}
        ),
    ]
