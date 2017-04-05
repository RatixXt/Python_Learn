import random
import json


def to_json(function_to_decorate):
    def wrapper(*args, **kwargs):
        data = function_to_decorate(*args, **kwargs)
        if isinstance(data, dict):
            data = json.dumps(data)
        return data
    return wrapper


@to_json
def example_func():
    if random.randint(0, 1):
        return {'message': '''I'm dictionary and you can convert me to JSON''', 'check_it': None}
        # Формат JSON и обычные словарь в Питоне внешне не различимы, но JSON берет свое начало в JS,
        # поэтому он преобразует None в null, что и будет проверкой кодирования в JSON
    else:
        return ["I'm just a simple string data", "And I'm too!", "But together we are List!"]


res = example_func()
# Дополнительная проверка, тип данных, очевидно, что словарь имел бы тип dict, но данные в JSON будут иметь тип str
print('data:{}, type:{}'.format(res, type(res)))

