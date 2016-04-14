
from django.shortcuts import render_to_response

from social.pipeline.partial import partial


@partial
def get_user_description(backend, details, response, is_new=False, *args, **kwargs):
    if backend.name == 'pocket' and is_new:
        data = backend.strategy.request_data()
        if data.get('description') is None:
            return render_to_response(
                'users/user_extra_data_form.html',
                {'pocket_usr': details, },
            )
        else:
            return {
                'nickname': data.get('nickname'),
                'description': data.get('description'),
            }


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'pocket':
        is_new = kwargs.get('is_new')
        if is_new:
            user.nickname = kwargs.get('nickname')
            user.description = kwargs.get('description')
            user.save()
