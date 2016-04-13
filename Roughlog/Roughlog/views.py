from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse


def home(request):
    if request.user.is_active:
        return redirect(
            reverse(
                'my-page',
                kwargs={
                    "slug": request.user.nickname,
                },
            )
        )

    return render(
        request,
        "home.html",
        context={},
    )
