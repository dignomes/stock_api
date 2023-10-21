import random
from typing import Dict, List, Literal, cast

import numpy as np
import numpy.typing as npt
from annoy import AnnoyIndex

from stock.models import Stock

ANNOY_METRIC = cast(Literal, "angular")
VECTOR_DIMENSIONS = 768
MODEL_PATH = "stock/services/model.ann"


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

        recommendations_from_model = self.get_recommendations_from_model(
            user_reacted_ids,
            numbers_of_all_companies,
            user_vector,
        )
        return [Stock.objects.get(id=i) for i in recommendations_from_model]

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
            numbers_of_all_companies: int,
            user_vector: npt.ArrayLike,
    ) -> List[int]:

        return [i for i in self.annoy_model.get_nns_by_vector(user_vector, numbers_of_all_companies//2) if
                i not in filtered_ids][:5]

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
            numbers_of_all_companies: int,
            ids_for_exclude: List[int],
    ) -> List[int]:
        return [
            company_id
            for company_id in range(numbers_of_all_companies)
            if company_id not in ids_for_exclude
        ]

    @staticmethod
    def __calculate_user_vector(user_features: np.ndarray) -> np.ndarray:
        return np.mean(user_features, axis=0).astype("float32")
