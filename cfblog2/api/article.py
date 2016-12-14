# -*- encoding: utf-8 -*-
from cfblog2 import db
from cfblog2.api import APICore, APICallException
from cfblog2.core.models import ArticleEntry as ArticleModel
from cfblog2.core.utils import model_obj_to_dict
from cfblog2.restful.resource import ResourceFilter
from . import api


class ArticleException(APICallException):
    pass


@api.resource("/article")
class Article(APICore):
    name = "Article"
    desc = "Article api"
    need_auth = False

    def __init__(self, *args, **kwargs):
        super(Article, self).__init__(*args, **kwargs)

    """Post article api"""
    @ResourceFilter(methods=["post"])
    def create(self, params):
        # TODO use param validator
        new_article = ArticleModel()
        new_article.title = params["title"]
        new_article.content = params["content"]
        new_article.slug = params["slug"]
        content_format = params.get("format", ArticleModel.ArticleFormat.PlainText)
        new_article.content_format = content_format
        db.session.add(new_article)
        db.session.commit()
        return model_obj_to_dict(new_article)

    """ article get api"""
    @ResourceFilter(methods=["get"])
    def retrieve_all(self, params):
        result = []
        rows = ArticleModel.query.all()
        for b in rows:
            result.append(model_obj_to_dict(b))
        return result

    @ResourceFilter("/<int:article_id>", methods=["get"])
    def retrieve_one(self, params, article_id):
        article = self.query_by_id(article_id).first()
        if article is None:
            return None
        else:
            return model_obj_to_dict(article)

    @ResourceFilter("/<int:article_id>", methods=["delete"])
    def delete_one(self, params, article_id):
        delete_count = self.query_by_id(article_id).delete()
        db.session.commit()

        return {"count": delete_count}

    @ResourceFilter("/<int:article_id>", methods=["patch"])
    def update_one(self, params, article_id):
        article = self.query_by_id(article_id).first()
        if article is None:
            return None

        article.title = params["title"]
        article.content = params["content"]
        article.slug = params["slug"]
        db.session.commit()
        return model_obj_to_dict(article)

    # noinspection PyMethodMayBeStatic
    def query_by_id(self, article_id):
        return ArticleModel.query.filter_by(id=article_id)
