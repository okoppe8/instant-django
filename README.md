instant-django
====

簡単なCRUD操作を行うDjangoのアプリケーションです。
モデル(app/models.py)の編集とマイグレーション、データ表示の変更だけで自分用のアプリケーションとして使うことができます。
使い方等は以下の記事を参照してください。

[Qiita: [Python] テンプレートアプリを使った業務用Webアプリケーション高速開発法の紹介【チュートリアル形式】](https://qiita.com/okoppe8/items/4cc0f87ea933749f5a49)


Instant-django is a practical sample project of Django.

Instant-django has a sample model and basic CRUD views.

You can complete a simple CRUD WebApp with a few edits and commands.

## Requirement

```
Django==2.1.1
django-crispy-forms==1.7.2
django-filter==2.0.0
pytz==2018.5
```

## Usage

Steps

1. Git clone this project
2. Edit modelfile `app/models.py`
3. Run `makemigrations` and `migrate`
4. Edit HTML files `templates/item_filter.html` and `item_detail_contents.html`

If you use it production environment, you must replace `settings.SECRET_KEY`.

## Contribution

I wrote this for Japanese python beginners.

I would appreciate if you clone this project and replace japanese code with your language for your country's python beginners.

## Licence

[WTFPL](http://www.wtfpl.net/txt/copying/)

## Author

Kawase Tomohiro
