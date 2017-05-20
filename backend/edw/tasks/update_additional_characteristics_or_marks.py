# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from celery import shared_task

from edw.models.term import TermModel
from edw.models.entity import EntityModel
from edw.models.related import AdditionalEntityCharacteristicOrMarkModel

#@shared_task(name='update_entities_additional_characteristics_or_marks')
def update_entities_additional_characteristics_or_marks(
        entities_ids, to_set_term_id, value, view_class, to_unset_term_id
    ):
    does_not_exist_entities_ids = []
    does_not_exist_terms_ids = []

    to_set_term = None
    if to_set_term_id is not None:
        try:
            to_set_term = TermModel.objects.attribute_is_characteristic_or_mark().get(
                id=to_set_term_id
            )
        except TermModel.DoesNotExist:
            does_not_exist_terms_ids.append(to_set_term_id)
    
    to_unset_term = None
    if to_unset_term_id is not None:
        try:
            to_unset_term = TermModel.objects.attribute_is_characteristic_or_mark().get(
                id=to_unset_term_id
            )
        except TermModel.DoesNotExist:
            does_not_exist_terms_ids.append(to_unset_term_id)

    #TODO: value and view class are empty
    for entity_id in entities_ids:
        try:
            entity = EntityModel.objects.get(id=entity_id)
        except EntityModel.DoesNotExist:
            does_not_exist_entities_ids.append(entity_id)
        else:
            if to_set_term:
                AdditionalEntityCharacteristicOrMarkModel.objects.get_or_create(
                    entity=entity,
                    term=to_set_term,
                    value=value,
                    view_class=view_class,
                )
            if to_unset_term:
                AdditionalEntityCharacteristicOrMarkModel.objects.filter(
                    entity=entity,
                    term=to_unset_term,
                ).delete()

    return {
        'entities_ids': entities_ids,
        'to_set_term_id': to_set_term_id,
        'to_unset_term_id': to_unset_term_id,
        'does_not_exist_entities_ids': does_not_exist_entities_ids,
        'does_not_exist_terms_ids': does_not_exist_terms_ids,
    }

