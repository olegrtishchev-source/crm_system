"""Создаёт группы-роли (Администратор, Оператор, Маркетолог, Менеджер)
и назначает им права на модели проекта.

Права модели (view/add/change/delete) появляются в базе не сразу при
применении миграций, а только после сигнала ``post_migrate`` — при первом
запуске ``migrate`` на «чистой» базе он сработает лишь после того, как
применятся вообще все миграции. Поэтому здесь права создаются вручную
через ``create_permissions`` перед тем, как назначить их группам.
"""

import operator
from functools import reduce

from django.apps import apps as django_apps
from django.contrib.auth.management import create_permissions
from django.db import migrations
from django.db.models import Q

ROLE_PERMISSIONS: dict[str, list[tuple[str, str]]] = {
    "Администратор": [
        ("auth", "add_user"),
        ("auth", "change_user"),
        ("auth", "delete_user"),
        ("auth", "view_user"),
        ("auth", "add_group"),
        ("auth", "change_group"),
        ("auth", "delete_group"),
        ("auth", "view_group"),
        ("products", "view_product"),
        ("advertisements", "view_advertisement"),
        ("leads", "view_lead"),
        ("contracts", "view_contract"),
        ("customers", "view_customer"),
    ],
    "Оператор": [
        ("leads", "add_lead"),
        ("leads", "change_lead"),
        ("leads", "delete_lead"),
        ("leads", "view_lead"),
        ("advertisements", "view_advertisement"),
    ],
    "Маркетолог": [
        ("products", "add_product"),
        ("products", "change_product"),
        ("products", "delete_product"),
        ("products", "view_product"),
        ("advertisements", "add_advertisement"),
        ("advertisements", "change_advertisement"),
        ("advertisements", "delete_advertisement"),
        ("advertisements", "view_advertisement"),
    ],
    "Менеджер": [
        ("leads", "view_lead"),
        ("customers", "add_customer"),
        ("customers", "change_customer"),
        ("customers", "delete_customer"),
        ("customers", "view_customer"),
        ("contracts", "add_contract"),
        ("contracts", "change_contract"),
        ("contracts", "delete_contract"),
        ("contracts", "view_contract"),
        ("advertisements", "view_advertisement"),
    ],
}


def create_roles(apps, schema_editor):  # pylint: disable=unused-argument
    """Создаёт права (при необходимости) и роли с назначенными правами."""
    for app_config in django_apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, verbosity=0)
        app_config.models_module = None

    group_model = apps.get_model("auth", "Group")
    permission_model = apps.get_model("auth", "Permission")

    for role_name, codenames in ROLE_PERMISSIONS.items():
        group, _ = group_model.objects.get_or_create(name=role_name)
        query = reduce(
            operator.or_,
            (
                Q(content_type__app_label=app_label, codename=codename)
                for app_label, codename in codenames
            ),
        )
        group.permissions.set(permission_model.objects.filter(query))


def delete_roles(apps, schema_editor):  # pylint: disable=unused-argument
    """Откатывает миграцию: удаляет созданные роли."""
    group_model = apps.get_model("auth", "Group")
    group_model.objects.filter(name__in=ROLE_PERMISSIONS.keys()).delete()


class Migration(migrations.Migration):
    """Данные: роли-группы для CRM."""

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("products", "0001_initial"),
        ("advertisements", "0001_initial"),
        ("leads", "0001_initial"),
        ("contracts", "0001_initial"),
        ("customers", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_roles, delete_roles),
    ]
