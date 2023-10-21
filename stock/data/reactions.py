from typing import List

from stock.models import Reaction, Stock, UserProfile


class ReactionService:
    @staticmethod
    def create_reaction(account_id: str, stock_id: int, reaction_str: str):
        user = UserProfile.objects.get_or_create(uid=account_id)
        stock = Stock.objects.get(pk=stock_id)
        reaction = Reaction.objects.create(
            account=user[0], stock=stock, reaction=reaction_str,
        )
        reaction.save()
        return reaction

    @staticmethod
    def get_user_reactions(user_id: str) -> List[Reaction]:

        user = UserProfile.objects.get_or_create(uid=1)
        return Reaction.objects.filter(account=user[0].id)
