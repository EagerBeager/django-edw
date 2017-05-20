#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext_lazy as _
from django.template.response import TemplateResponse
from django.contrib.admin import helpers
from django.contrib.admin.utils import model_ngettext

from edw.admin.entity.forms import EntitiesUpdateAdditionalCharacteristicsOrMarksAdminForm

from edw.tasks import update_entities_additional_characteristics_or_marks


def update_additional_characteristics_or_marks(modeladmin, request, queryset):
    """
    Update additional marks for multiple entities
    """
    CHUNK_SIZE = getattr(settings, 'EDW_UPDATE_ADDITIONAL_CHARACTERISTICS_OR_MARKS_ACTION_CHUNK_SIZE', 100)

    opts = modeladmin.model._meta
    app_label = opts.app_label

    if request.POST.get('post'):
        form = EntitiesUpdateAdditionalCharacteristicsOrMarksAdminForm(request.POST)
        if form.is_valid():
            to_set_term = form.cleaned_data['to_set_term']
            to_unset_term = form.cleaned_data['to_unset_term']
            value = form.cleaned_data['value']
            view_class = form.cleaned_data['view_class']

            n = queryset.count()
            if n and ((to_set_term and value and view_class) or to_unset_term):
                i = 0
                tasks = []
                while i < n:
                    chunk = queryset[i:i + CHUNK_SIZE]
                    for obj in chunk:
                        obj_display = force_unicode(obj)
                        modeladmin.log_change(request, obj, obj_display)

                    #tasks.append(
                    #    update_entities_additional_characteristics_or_marks.si(
                    #    )
                    #)
                    update_entities_additional_characteristics_or_marks(
                        [x.id for x in chunk],
                        to_set_term.id if to_set_term else None,
                        value if value else None,
                        view_class if view_class else None,
                        to_unset_term.id if to_unset_term else None
                    )
                    i += CHUNK_SIZE

                #chain(reduce(OR, tasks)).apply_async()

                modeladmin.message_user(request, _("Successfully proceed %(count)d %(items)s.") % {
                    "count": n, "items": model_ngettext(modeladmin.opts, n)
                })
            # Return None to display the change list page again.
            return None
    else:
        form = EntitiesUpdateAdditionalCharacteristicsOrMarksAdminForm()

    if len(queryset) == 1:
        objects_name = force_unicode(opts.verbose_name)
    else:
        objects_name = force_unicode(opts.verbose_name_plural)

    title = _("Update additional characteristics or marks for multiple entities")
    context = {
        "title": title,
        'form': form,
        "objects_name": objects_name,
        'queryset': queryset,
        "opts": opts,
        "app_label": app_label,
        'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
        'media': modeladmin.media,
    }
    # Display the confirmation page
    return TemplateResponse(request, "edw/admin/entities/actions/update_additional_characteristics_or_marks.html",
                            context, current_app=modeladmin.admin_site.name)


update_additional_characteristics_or_marks.short_description = \
    _("Modify additional characteristics or marks for selected %(verbose_name_plural)s")
#
