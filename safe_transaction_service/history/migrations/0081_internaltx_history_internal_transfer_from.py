# Generated by Django 5.0.3 on 2024-04-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0080_alter_multisigconfirmation_signature"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="internaltx",
            index=models.Index(
                condition=models.Q(("call_type", 0), ("value__gt", 0)),
                fields=["_from", "timestamp"],
                include=("ethereum_tx_id", "block_number"),
                name="history_internal_transfer_from",
            ),
        ),
    ]
