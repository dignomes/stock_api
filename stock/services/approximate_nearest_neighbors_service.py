import random
from typing import Dict, List, Literal, cast

import numpy as np
import numpy.typing as npt
from annoy import AnnoyIndex

from stock.models import Stock

ANNOY_METRIC = cast(Literal, "angular")
VECTOR_DIMENSIONS = 768
MODEL_PATH = "model.ann"


class ApproximateNearestNeighborsService:
    def __init__(self):
        self.annoy_model = AnnoyIndex(VECTOR_DIMENSIONS, ANNOY_METRIC)
        self.annoy_model.load(MODEL_PATH)

    def get_user_recommendations(
            self,
            user_liked_ids: List[int],
            user_reacted_ids: List[int],
    ) -> List[int]:
        user_vectors = self.get_vectors_by_ids(user_liked_ids)
        user_vector = self.__calculate_user_vector(user_vectors)

        numbers_of_all_companies = self.annoy_model.get_n_items()
        filtered_ids = self.__get_filtered_ids(numbers_of_all_companies, user_reacted_ids)

        recommendations_from_model = self.get_recommendations_from_model(
            filtered_ids,
            user_vector,
        )
        return Stock.objects.filter(stock_id__in=recommendations_from_model)

    def get_nearest_vectors_ids_by_vector(
            self,
            vector: npt.ArrayLike,
            number_of_vectors: int = 10,
    ) -> np.ndarray:
        vector_ids = self.annoy_model.get_nns_by_vector(vector, number_of_vectors)

        return np.array(
            [self.annoy_model.get_item_vector(vector_id) for vector_id in vector_ids],
        )

    def get_recommendations_from_model(
            self,
            filtered_ids: List[int],
            user_vector: npt.ArrayLike,
    ) -> List[int]:
        small_model = AnnoyIndex(VECTOR_DIMENSIONS, ANNOY_METRIC)
        for meme_id in filtered_ids:
            small_model.add_item(meme_id, self.annoy_model.get_item_vector(meme_id))

        small_model.build(10)
        return small_model.get_nns_by_vector(user_vector, 5)

    def get_vectors_by_ids(self, company_ids: List[int]) -> np.ndarray:
        return np.array(
            [self.annoy_model.get_item_vector(company_id) for company_id in
             company_ids],
        )

    @staticmethod
    def __get_random_companies(
            filtered_ids: List[int],
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

    @staticmethod
    def __calculate_user_vector(user_features: np.ndarray) -> np.ndarray:
        return np.mean(user_features, axis=0).astype("float32")
