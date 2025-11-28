from django.http import JsonResponse


def health(request):
    """Simple health endpoint for the OctoFit tracker API."""
    return JsonResponse({
        "status": "ok",
        "service": "octofit-tracker",
    })


def activities_list(request):
    """Placeholder activities endpoint returning an empty list."""
    return JsonResponse({
        "activities": [],
    })
