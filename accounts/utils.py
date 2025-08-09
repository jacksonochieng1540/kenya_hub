from .models import Badge
from django.contrib import messages

def award_badge_if_needed(request, user):
    # Gold
    if user.reputation >= 1000 and not user.badges.filter(badge_type='gold').exists():
        Badge.objects.create(user=user, badge_type='gold', reason="Reached 1000 reputation")
        messages.success(request, "🏆 Congratulations! You earned a Gold Badge!")

    # Silver
    elif user.reputation >= 500 and not user.badges.filter(badge_type='silver').exists():
        Badge.objects.create(user=user, badge_type='silver', reason="Reached 500 reputation")
        messages.success(request, "🥈 Well done! You earned a Silver Badge!")

    # Bronze
    elif user.reputation >= 100 and not user.badges.filter(badge_type='bronze').exists():
        Badge.objects.create(user=user, badge_type='bronze', reason="Reached 100 reputation")
        messages.success(request, "🥉 Nice! You earned a Bronze Badge!")
