import uuid
import random
from typing import Any, get_type_hints, get_origin, Annotated, get_args
import rstr
from src.main.api.generators.creation_rule import CreationRule


class RandomModelGenerator:
    @staticmethod
    def generate(cls: type, **overrides) -> Any:
        type_hints = get_type_hints(cls, include_extras=True)
        init_data = {}

        for field_name, annotated_type in type_hints.items():

            if field_name in overrides:
                init_data[field_name] = overrides[field_name]
                continue

            rule = None
            actual_type = annotated_type

            if get_origin(annotated_type) is Annotated:
                actual_type, *annotations = get_args(annotated_type)
                for ann in annotations:
                    if isinstance(ann, CreationRule):
                        rule = ann

            if rule:
                value = RandomModelGenerator._generate_from_regex(rule.regex, actual_type)
            else:
                value = RandomModelGenerator.generate_value(actual_type)

            init_data[field_name] = value

        return cls(**init_data)

    @staticmethod
    def _generate_from_regex(regex: str, field_type: type):
        generated = rstr.xeger(regex)
        if field_type is int:
            return int(generated)
        if field_type is float:
            return float(generated)
        return generated

    @staticmethod
    def generate_value(
            field_type: type,
            min_int:int = 1,
            max_int:int = 9999,
            min_float:float = 0,
            max_float:float = 100
                       ) -> Any:
        if field_type is str:
            return str(uuid.uuid4())[:8]
        elif field_type is int:
            return random.randint(min_int, max_int)
        elif field_type is float:
            return round(random.uniform(min_float, max_float ), 2)
        elif field_type is bool:
            return random.choice([True, False])
        elif field_type is list:
            return [str(uuid.uuid4())[:5]] #возвращает список [] из 1 строки
        elif isinstance(field_type, type):
            return RandomModelGenerator.generate(field_type) #рекурсия для вложенных моделей если тип это класс
        return None

