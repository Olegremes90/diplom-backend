# Generated by Django 4.2.6 on 2023-10-17 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("descrip", models.TextField(max_length=2500)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Engine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("descrip", models.TextField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name="Lead",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("descrip", models.TextField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name="Machine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number_machine", models.CharField(max_length=100)),
                ("number_engine", models.CharField(max_length=100)),
                ("number_transmisia", models.CharField(max_length=100)),
                ("number_lead", models.CharField(max_length=100)),
                ("number_steerable_bridge", models.CharField(max_length=100)),
                ("contract_postavka", models.TextField(max_length=250)),
                ("date_otgruzka", models.DateField(auto_now_add=True)),
                ("consignee", models.TextField(max_length=250)),
                ("adress", models.CharField(max_length=200)),
                ("complectation", models.TextField(max_length=1000)),
                (
                    "client_model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="silant.client"
                    ),
                ),
                (
                    "lead_model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="silant.lead"
                    ),
                ),
                (
                    "model_engine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="silant.engine"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recovery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("descrip", models.TextField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("descrip", models.TextField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name="Steerable_Bridge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("descrip", models.TextField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name="Technica",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("descrip", models.TextField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name="Transmisia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("descrip", models.TextField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name="Usel_Refusal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("descrip", models.TextField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name="Vidi_TO",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("descrip", models.TextField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name="TO",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_to", models.DateField()),
                ("narabotka", models.IntegerField()),
                ("number_zakaza", models.CharField(max_length=100)),
                ("data_zakaza", models.DateField()),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="silant.machine"
                    ),
                ),
                (
                    "service_company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="silant.service"
                    ),
                ),
                (
                    "vid_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="silant.vidi_to"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="machine",
            name="model_steerable_bridge",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="silant.steerable_bridge",
            ),
        ),
        migrations.AddField(
            model_name="machine",
            name="model_technic",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="silant.technica"
            ),
        ),
        migrations.AddField(
            model_name="machine",
            name="model_transmisia",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="silant.transmisia"
            ),
        ),
        migrations.AddField(
            model_name="machine",
            name="service_model",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="silant.service"
            ),
        ),
        migrations.CreateModel(
            name="Complaint",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_refusal", models.DateField()),
                ("working_off", models.IntegerField()),
                ("description", models.TextField(max_length=1000)),
                ("spare_parts", models.TextField(max_length=1000)),
                ("date_recovery", models.DateField()),
                (
                    "car_complaint",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="silant.machine"
                    ),
                ),
                (
                    "recovery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="silant.recovery",
                    ),
                ),
                (
                    "service_org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="silant.service"
                    ),
                ),
                (
                    "usel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="silant.usel_refusal",
                    ),
                ),
            ],
        ),
    ]
