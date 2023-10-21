from typing import List

from accounts.models import Account
from stock.models import Reaction, Stock


class ReactionService:
    @staticmethod
    def create_reaction(account_id: int, stock_id: int, reaction: str):
        user = Account.objects.get_or_create(pk=account_id)
        stock = Stock.objects.get(pk=stock_id)
        reaction = Reaction.objects.create(
            user=user, stock=stock, reaction=reaction,
        )
        reaction.save()


    @staticmethod
    def get_user_reactions(user_id: int) -> List[Reaction]:
        user = Account.objects.get_or_create(pk=user_id)
        return Reaction.objects.filter(user=user)
