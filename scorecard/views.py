#from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from scorecard.models import Theme, Objective, Outcome, StaticContent
import operator


def index(request):
    theme_list = Theme.objects.all().extra(order_by=['themeid']).exclude(foundation=True)
    num_themes = len(theme_list)
    try:
        foundation_theme = Theme.objects.get(foundation=True)
    except Theme.DoesNotExist:
        foundation_theme = False
    return render_to_response('index.html', {
        'theme_list': theme_list,
        'num_themes': num_themes,
        'foundation_theme': foundation_theme,
    })


def theme(request, themeid):
    active_theme = get_object_or_404(Theme, themeid=themeid)
    theme_list = Theme.objects.all().extra(order_by=['themeid']).exclude(foundation=True)
    try:
        foundation_theme = Theme.objects.get(foundation=True)
    except Theme.DoesNotExist:
        foundation_theme = False

    return render_to_response('theme.html', {
        'active_theme': active_theme,
        'theme_list': theme_list,
        'foundation_theme': foundation_theme,
    })


def outcome(request, themeid, objectiveid, outcomeid):
    try:
        foundation_theme = Theme.objects.get(foundation=True)
    except Theme.DoesNotExist:
        foundation_theme = False

    theme_list = Theme.objects.all().extra(order_by=['themeid']).exclude(foundation=True)
    return render_to_response('outcome.html', {
        'active_theme': get_object_or_404(Theme, themeid=themeid),
        'active_objective': get_object_or_404(Objective, objectiveid=objectiveid, theme=themeid),
        'active_outcome': get_object_or_404(Outcome.objects.select_related(), objective=objectiveid, outcomeid=outcomeid),
        'theme_list': theme_list,
        'foundation_theme': foundation_theme,
    })


def staticpage(request, pageurl):
    try:
        foundation_theme = Theme.objects.get(foundation=True)
    except Theme.DoesNotExist:
        foundation_theme = False

    return render_to_response('static.html', {
        'page': get_object_or_404(StaticContent, pageurl=pageurl),
        'theme_list': Theme.objects.all().extra(order_by=['themeid']).exclude(foundation=True),
        'foundation_theme': foundation_theme,
    })
