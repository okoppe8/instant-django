from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    カスタムユーザー データ定義クラス

    ユーザーの管理項目を増やしたい場合はここにフィールドを定義します。
    例：住所、電話番号など
    """

    # first_name、last_nameの代わりにfull_nameを用意する
    full_name = models.CharField(
        verbose_name='氏名',
        max_length=100,
        blank=True
    )

    # スタッフ権限のデフォルトをTrueに変更する
    # ※ 原則ログインして利用することを想定している。

    is_staff = models.BooleanField(
        _('staff status'),
        default=True,
    )

    # get_full_name()の変更
    def get_full_name(self):
        if self.full_name:
            return self.full_name
        else:
            return self.username + '（氏名未登録）'

    # 選択リストでの表示
    def __str__(self):
        return self.get_full_name()
