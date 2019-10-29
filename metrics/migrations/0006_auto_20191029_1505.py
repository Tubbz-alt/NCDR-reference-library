# Generated by Django 2.1.7 on 2019-10-29 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("metrics", "0005_metriclead_teamlead")]

    operations = [
        migrations.AddField(
            model_name="metric",
            name="metric_lead",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="metrics.MetricLead",
            ),
        ),
        migrations.AddField(
            model_name="metric",
            name="team_lead",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="metrics.TeamLead",
            ),
        ),
    ]
