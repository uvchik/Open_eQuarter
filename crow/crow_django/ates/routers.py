class AtesRouter(object):
    def db_for_read(self, model, **hints):
        "Point all operations on ates models to 'atesdb'"
        if model._meta.app_label == 'ates':
            return 'atesdb'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on ates models to 'atesdb'"
        if model._meta.app_label == 'ates':
            return 'atesdb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in ates app"
        if obj1._meta.app_label == 'ates' and obj2._meta.app_label == 'ates':
            return True
        # Allow if neither is ates app
        elif 'ates' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_migrate(self, db, model):
        if db == 'atesdb' or model._meta.app_label == "ates":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True