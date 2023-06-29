from django.db.models import Q


def select_all_model(model):
    return model.objects.all()


def category_filter(model, id1, id2):
    get_filter_category = model.objects.filter(~Q(id=id1)).filter(~Q(id=id2))
    return get_filter_category
