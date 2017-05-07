# -*- encoding: utf -*-


def model_obj_to_dict(model):
    # TODO optimize Consider a good way?
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}

