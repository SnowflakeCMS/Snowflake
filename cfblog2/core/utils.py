#-*- encoding: utf -*-


def model_obj_to_dict(model):
    # TODO optimize Consider a good way?
    ret_dict = dict(model.__dict__)
    ret_dict.pop("_sa_instance_state", None)
    return ret_dict
