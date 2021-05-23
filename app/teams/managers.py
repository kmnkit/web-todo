from django.db.models import Q, Manager


class CustomMemberManager(Manager):
    """Additional Manager function"""

    def add_member(self, user, team):
        self.create(user=user, team=team)

    def remove_member(self, user, team):
        self.delete(user=user, team=team)

    def set_nickname(self, user, team, nickname):
        member = self.get(Q(user=user) & Q(team=team))
        member.nickname = nickname
        member.save()
