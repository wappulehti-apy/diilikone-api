from flask import url_for
from flask.ext.login import current_user
from flask_admin.contrib.sqla import ModelView
from jinja2 import Markup


class AuthRequired(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated()


class UserView(AuthRequired):
    column_searchable_list = ('first_name', 'last_name')


class DealView(AuthRequired):
    column_list = ('salesperson', 'deal_group', 'size')

    def _salesperson_formatter(view, context, model, name):
        return Markup(
            "<a href='%s'>%s</a>" % (
                url_for('user.edit_view', id=model.salesperson.id),
                model.salesperson.first_name + ' ' + model.salesperson.last_name


            )
        ) if model.salesperson else ""

    def _deal_group_formatter(view, context, model, name):
        return Markup(
            "<a href='%s'>%s</a>" % (
                url_for('dealgroup.edit_view', id=model.deal_group.id),
                model.deal_group.name


            )
        ) if model.deal_group else ""

    column_formatters = {
        'salesperson': _salesperson_formatter,
        'deal_group': _deal_group_formatter
    }


class ProductView(AuthRequired):
    column_list = ('name', 'left_in_stock')


class DealGroupView(AuthRequired):
    column_list = ('name', 'total_size')
