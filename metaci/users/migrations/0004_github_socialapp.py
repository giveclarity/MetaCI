# Generated by Django 3.1.7 on 2021-03-19 19:16

from django.db import migrations


def update_github_socialapp(apps, schema_editor):
    # Make sure there's a github SocialApp,
    # and remove its client_id and secret
    # (they'll be used from environment variable-based settings)
    SocialApp = apps.get_model("socialaccount", "SocialApp")
    try:
        app = SocialApp.objects.get(provider="github")
    except SocialApp.DoesNotExist:
        app = SocialApp(provider="github")
    app.name = "GitHub"
    app.client_id = "-"
    app.secret = ""
    app.save()


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_auto_20210304_0926"),
    ]

    operations = [migrations.RunPython(update_github_socialapp)]