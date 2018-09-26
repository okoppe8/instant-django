from django import template

register = template.Library()


@register.simple_tag
def url_replace(request, field, value):
    """
    ページ間で検索パラメータを引き継ぐ
    参考：http://hideharaaws.hatenablog.com/entry/2015/01/16/002813
    """
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
