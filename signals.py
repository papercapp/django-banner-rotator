# coding=utf-8


from django.dispatch import Signal



banner_viewed = Signal(providing_args=["info", "request"])
banner_clicked = Signal(providing_args=["info", "request"])