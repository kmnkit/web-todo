from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def on_team(context, team):
    user = context.request.user
    return user in team.members.all()