import os

from flask import Flask

import pkgutil
import importlib

from .extensions import cors, db, mail, login_manager


class Application(Flask):
    def __init__(self, environment=None):
        super(Application, self).__init__(__name__)
        self._init_settings(environment)
        self._init_extensions()
        self._init_views()
        self._init_admin_views()
        self.config['KONCH_CONTEXT'] = self._make_shell_context()
        self.config['KONCH_SHELL'] = 'ipy'

    def _init_settings(self, environment=None):
        if environment is None:
            environment = os.environ.get('FLASK_ENV', 'development')
        settings_module = 'diilikone.settings.' + environment
        self.config.from_object(settings_module)

    def _init_extensions(self):
        cors.init_app(self)
        db.init_app(self)
        mail.init_app(self)
        login_manager.init_app(self)

    def _init_views(self):
        from .views.dummy import dummy
        from .views.deals import deals
        from .views.deal_groups import deal_groups
        from .views.provision import provision
        from .views.product_types import product_types
        self.register_blueprint(dummy)
        self.register_blueprint(deals)
        self.register_blueprint(deal_groups)
        self.register_blueprint(provision)
        self.register_blueprint(product_types)

    def _init_admin_views(self):
        from flask_admin import Admin
        from diilikone.models import User, Deal, DealGroup, ProductType
        from diilikone.admin.view import (
            DealGroupView,
            DealView,
            ProductView,
            UserView
        )
        from diilikone.admin.login import admin_login

        self.register_blueprint(admin_login)

        admin = Admin(self)
        admin.add_view(UserView(User, db.session))
        admin.add_view(DealView(Deal, db.session))
        admin.add_view(DealGroupView(DealGroup, db.session))
        admin.add_view(ProductView(ProductType, db.session))

    def _make_shell_context(self):  # pragma: no cover
        load_models()
        context = super().make_shell_context()
        context['db'] = db
        context.update(db.Model._decl_class_registry)
        return context


def load_models():
    """
    Load models from the subpackages of the application.

    This is implemented by iterating over the subpackages of the
    application and trying to import `models` module/package under the
    subpackage.
    """

    allowed_folders = [
        __name__
    ]

    for loader, name, is_package in pkgutil.iter_modules(allowed_folders):
        if is_package:
            module_path = loader.path.replace('/', '.')
            try:
                importlib.import_module(
                    name='.'.join([module_path, name, 'models']),
                    package=__name__
                )
            except ImportError:
                pass
