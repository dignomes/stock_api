import random
from typing import Dict, List, Literal, cast

import numpy as np
import numpy.typing as npt
from annoy import AnnoyIndex
from loguru import logger

from service.config import MODEL_PATH, VECTOR_DIMENSIONS

ANNOY_METRIC = cast(Literal, "angular")


class ApproximateNearestNeighborsService:
    def __init__(self):
        self.annoy_model = AnnoyIndex(VECTOR_DIMENSIONS, ANNOY_METRIC)
        self.annoy_model.load(MODEL_PATH)

    def get_user_recommendations(
            self,
            user_liked_ids: List[int],
            user_reacted_ids: List[int],
    ) -> List[int]:
        user_vectors = self.get_vectors_by_ids(user_reacted_ids)
        user_vector = random.choice(user_vectors)
        numbers_of_all_companies = self.annoy_model.get_n_items()
        recommendations_from_model = self.get_nearest_vectors_ids_by_vector(user_vector)

        filtered_ids = random.sample(
            self.__get_filtered_ids(numbers_of_all_companies, user_reacted_ids),
            numbers_of_all_companies
        )
        random_companies = self.__get_random_companies(filtered_ids)

        return recommendations_from_model

    def get_nearest_vectors_ids_by_vector(
            self,
            vector: npt.ArrayLike,
            number_of_vectors: int = 10,
    ) -> np.ndarray:
        vector_ids = self.annoy_model.get_nns_by_vector(vector, number_of_vectors)

        return np.array(
            [self.annoy_model.get_item_vector(vector_id) for vector_id in vector_ids],
        )

    def get_vectors_by_ids(self, company_ids: List[int]) -> np.ndarray:
        return np.array(
            [self.annoy_model.get_item_vector(company_id) for company_id in
             company_ids],
        )

    @staticmethod
    def __get_random_companies(
            filtered_ids: list[int],
            number: int = 5,
    ) -> List[int]:
        return random.sample(filtered_ids, k=number)

    @staticmethod
    def __get_filtered_ids(
            numbers_of_all_memes: int,
            memes_id_for_exclude: List[int],
    ) -> List[int]:
        return [
            meme_id
            for meme_id in range(numbers_of_all_memes)
            if meme_id not in memes_id_for_exclude
        ]
