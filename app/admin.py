from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    管理画面上の動作の設定
      項目の表示非表示や検索項目の指定が可能
    参考：
    ・公式 The Django admin site
    https://docs.djangoproject.com/ja/2.1/ref/contrib/admin/
    ・Django 管理画面逆引きメモ
    https://qiita.com/zenwerk/items/044c149d93db097cdaf8
    ・ModelAdminをカスタマイズする方法
    https://qiita.com/cnloni/items/9d3ed9394c2ad935d1f7#modeladmin%E3%82%92%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%9E%E3%82%A4%E3%82%BA%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95
    """
    class Meta:
        pass
