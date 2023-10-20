from typing import List

from accounts.models import Account
from stock.models import Reactions, Stock


class ReactionService:
    @staticmethod
    def create_reaction(account_id: int, stock_id: int, reaction: str):
        user = Account.objects.filter(
            id=account_id
        ).first()
        stock = Stock.objects.filter(id=stock_id)
        Reactions.objects.create(
            user=user, stock=stock, reaction=reaction,
        )

    @staticmethod
    def get_user_reactions(user_id: int) -> List[Reactions]:
        return Reactions.objects.filter(
            user_id=user_id
        )
