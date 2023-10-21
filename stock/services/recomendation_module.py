import random
from typing import List

from stock.data.reactions import ReactionService
from stock.models import Stock
from stock.services.approximate_nearest_neighbors_service import ApproximateNearestNeighborsService


class Reactions:
    LIKE = "LIKE"
    DISLIKE = "DISLIKE"
    NOTHING = "NOTHING"


class RecomendationSystem:
    def __init__(self):
        self.__ann_service = ApproximateNearestNeighborsService()
        self.__reaction_service = ReactionService()

    def get_recommendation(self, user_id: int) -> List[int]:
        # get all reactions for exclude them
        self.__reaction_service = ReactionService()
        user_reactions = self.__reaction_service.get_user_reactions(user_id)

        user_reactions_ids = [user_reaction.id for user_reaction in user_reactions]
        user_liked_ids = [
            user_reaction.id
            for user_reaction in user_reactions
            if user_reaction.reaction == Reactions.LIKE
        ]

        if user_reactions_ids:
            return self.__ann_service.get_user_recommendations(
                user_liked_ids,
                user_reactions_ids,
            )
        return [stock for stock in self.get_init_companies()]

    @staticmethod
    def get_init_companies():
        items = list(Stock.objects.all())
        return random.sample(items, 10)

print(RecomendationSystem().get_recommendation(123))