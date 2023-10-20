from typing import List

from stock.data.reactions import ReactionService
from stock.services.approximate_nearest_neighbors_service import ApproximateNearestNeighborsService


class Reactions:
    LIKE = "LIKE"
    DISLIKE = "DISLIKE"
    NOTHING = "NOTHING"


class RecomendationSystem:
    def __init__(self):
        self.__ann_service = ApproximateNearestNeighborsService()
        self.__reaction_service = ReactionService()
        self.__company_service = CompanyService()

    def get_memes_recommendation(self, user_id: int) -> List[int]:
        # get all reactions for exclude them
        self.__reaction_service = ReactionService()
        user_reactions = self.__reaction_service.get_user_reactions(user_id)

        user_reactions_ids = [user_reaction.meme_id for user_reaction in user_reactions]
        user_liked_memes_ids = [
            user_reaction.meme_id
            for user_reaction in user_reactions
            if user_reaction.reaction == Reactions.LIKE
        ]

        if user_reactions_ids:
            return self.__ann_service.get_user_recommendations(
                user_liked_memes_ids,
                user_reactions_ids,
            )

        return [company.id for company in self.__company_service.get_init_companies()]
