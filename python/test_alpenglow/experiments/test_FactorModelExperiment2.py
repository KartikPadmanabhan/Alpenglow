import alpenglow as prs
import alpenglow.Getter as rs
import alpenglow.experiments
import alpenglow.evaluation
import pandas as pd
import math


class TestFactorModelExperiment:
    def test_factorModelExperiment2(self):
        factorModelExperiment = alpenglow.experiments.FactorModelExperiment2(
            top_k=100,
            seed=254938879,
            dimension=10,
            learning_rate=0.1,
            negative_rate=10
        )
        facRankings = factorModelExperiment.run("python/test_alpenglow/test_data_4", experimentType="online_id", verbose=True)
        assert facRankings.top_k == 100
        desired_ranks = [102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 1, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 3, 102, 102, 0, 102, 102, 102, 102, 102, 102, 102, 7, 102, 102, 102, 102, 102, 102, 102, 102, 1, 102, 102, 102, 1, 2, 20, 102, 102, 25, 102, 29, 102, 102, 102, 102, 102, 102, 21, 102, 8, 1, 17, 102, 102, 102, 102, 102, 102, 34, 102, 2, 102, 7, 102, 102, 102, 4, 102, 102, 43, 102, 21, 22, 102, 102, 102, 102, 102, 102, 3, 102, 2, 4, 102, 57, 42, 16, 14, 102, 102, 11, 102, 102, 102, 3, 28, 58, 56, 102, 9, 57, 102, 102, 21, 45, 102, 102, 102, 70, 3, 15, 102, 32, 43, 46, 5, 10, 9, 5, 102, 60, 102, 102, 41, 16, 59, 102, 68, 66, 60, 22, 23, 31, 102, 31, 102, 102, 49, 102, 17, 50, 102, 42, 59, 5, 0, 53, 102, 16, 102, 102, 32, 102, 102, 102, 102, 37, 102, 12, 14, 102, 102, 102, 102, 76, 60, 71, 102, 102, 64, 102, 40, 102, 75, 34, 34, 51, 102, 102, 59, 60, 102, 69, 16, 16, 2, 36, 2, 102, 102, 102, 102, 13, 102, 48, 102, 9, 102, 72, 32, 102, 102, 66, 24, 95, 20, 102, 102, 80, 98, 82, 58, 102, 95, 102, 6, 85, 60, 21, 24, 69, 9, 102, 102, 102, 102, 102, 12, 60, 102, 92, 16, 15, 44, 14, 102, 17, 100, 88, 56, 102, 102, 58, 102, 96, 6, 38, 102, 95, 30, 57, 100, 71, 0, 102, 39, 93, 102, 102, 102, 102, 1, 42, 12, 102, 102, 2, 102, 38, 83, 102, 21, 47, 52, 1, 94, 0, 102, 102, 102, 19, 102, 3, 12, 102, 100, 95, 102, 102, 102, 102, 100, 99, 73, 100, 1, 24, 100, 31, 102, 102, 102, 102, 100, 102, 100, 102, 100, 102, 0, 102, 10, 47, 57, 102, 30, 59, 27, 100, 49, 102, 38, 6, 102, 93, 102, 42, 5, 100, 5, 100, 102, 5, 100, 102, 100, 102, 9, 62, 14, 90, 65, 20, 9, 102, 41, 8, 102, 102, 0, 52, 13, 1, 102, 102, 102, 18, 87, 102, 27, 90, 102, 100, 11, 102, 35, 88, 100, 73, 100, 5, 22, 8, 102, 100, 61, 70, 2, 67, 30, 102, 102, 18, 45, 102, 68, 102, 87, 102, 61, 100, 15, 102, 102, 100, 100, 102, 100, 102, 102, 102, 102, 102, 41, 77, 100, 69, 27, 102, 66, 52, 30, 102, 1, 102, 12, 102, 82, 100, 38, 102, 102, 14, 102, 4, 87, 11, 100, 28, 100, 73, 100, 100, 100, 100, 39, 68, 100, 23, 71, 15, 57, 102, 46, 81, 102, 100, 0, 100, 11, 94, 100, 100, 100, 4, 7, 92, 100, 102, 11, 102, 100, 102, 100, 102, 62, 100, 102, 102, 102, 100, 102, 60, 100, 100, 10, 100, 102, 100, 0, 91, 82, 102, 102, 100, 46, 102, 83, 100, 100, 100, 16, 100, 87, 100, 102, 100, 100, 100, 59, 8, 39, 82, 93, 79, 100, 100, 102, 29, 6, 100, 34, 2, 102, 102, 11, 102, 100, 67, 102, 83, 102, 102, 100, 100, 102, 83, 48, 86, 74, 102, 102, 59, 100, 68, 17, 102, 100, 100, 31, 100, 28, 100, 102, 100, 10, 100, 4, 100, 70, 102, 100, 102, 100, 102, 65, 102, 100, 100, 100, 94, 102, 42, 102, 99, 100, 102, 102, 6, 77, 3, 102, 100, 100, 60, 14, 102, 55, 82, 102, 100, 102, 19, 100, 44, 100, 91, 100, 100, 102, 84, 102, 100, 100, 100, 100, 36, 6, 102, 100, 102, 56, 102, 102, 52, 100, 100, 100, 102, 60, 31, 100, 100, 69, 100, 100, 82, 67, 100, 79, 100, 69, 102, 102, 73, 102, 102, 69, 102, 100, 100, 102, 102, 100, 10, 100, 31, 100, 102, 52, 47, 102, 29, 102, 73, 60, 15, 100, 2, 100, 100, 17, 100, 58, 102, 100, 93, 8, 100, 100, 100, 23, 53, 71, 0, 100, 102, 100, 100, 102, 100, 102, 48, 49, 68, 100, 102, 29, 100, 78, 84, 100, 93, 93, 94, 100, 102, 102, 48, 100, 102, 100, 47, 100, 102, 100, 75, 100, 20, 81, 5, 102, 102, 44, 30, 100, 100, 102, 46, 99, 28, 102, 1, 85, 61, 77, 1, 100, 49, 5, 33, 100, 100, 65, 100, 100, 90, 100, 71, 102, 100, 60, 52, 97, 61, 102, 100, 69, 100, 100, 100, 93, 6, 79, 102, 100, 5, 100, 100, 102, 1, 24, 102, 102, 23, 100, 37, 54, 100, 94, 102, 98, 100, 100, 16, 102, 100, 43, 100, 100, 102, 45, 9, 26, 65, 100, 100, 100, 100, 100, 64, 39, 100, 100, 18, 58, 100, 57, 100, 70, 21, 71, 19, 100, 2, 34, 100, 28, 27, 100, 100, 100, 12, 40, 102, 102, 100, 102, 102, 47, 83, 71, 102, 3, 100, 100, 11, 100, 12, 100, 100, 102, 62, 100, 102, 102, 40, 100, 100, 100, 102, 100, 82, 1, 100, 100, 2, 52, 100, 1, 100, 102, 100, 100, 102, 102, 15, 100, 100, 36, 100, 102, 100, 94, 100, 102, 100, 22, 78, 100, 100, 100, 46, 6, 100, 7, 100, 100, 100, 7, 1, 100, 102, 18, 1, 69, 102, 100, 100, 42, 100, 61, 100, 102, 67, 100, 75, 102, 100, 102, 100, 90, 27, 84, 7, 4, 102, 15, 100, 100, 24, 102, 102, 19, 21, 3, 102, 100, 71, 41, 100, 102, 35, 16, 86, 100, 34, 102, 43, 100, 102, 102, 33, 102, 35, 102, 74, 100, 0, 12, 27, 100, 16, 100, 100, 27, 100, 100, 11, 102, 100, 29, 102, 41, 100, 100, 6, 100, 100, 86, 18, 45, 100, 100, 100, 66, 5, 100, 1, 0, 100, 100, 102, 4, 100, 16, 100, 27, 19, 102, 40, 100, 100, 11, 100, 100, 100, 100, 48, 33, 102]
        desired_ranks = list(map(lambda i: i + 1 if i < 100 else 101, desired_ranks))
        assert list(facRankings["rank"].fillna(101)) == desired_ranks