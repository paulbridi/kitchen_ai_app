import os
import pandas as pd
import gensim.downloader
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.utils import unpickle, pickle

def input_to_recipes_df(input_ingred:list, input_tags:list, df, model):
    """Take inputed ingredients, preference, recipes dataframe and return top 5 most similar recipes"""

    # df = pd.read_pickle(df_path)

    # # unpickle a pickled Doc2Vec model
    # model = unpickle(model_path)

    all_input = input_ingred + input_tags
    tokens = [word.strip(", ") for word in all_input]
    all_vectors = model.infer_vector(tokens)

    most_similar_all = model.dv.most_similar([all_vectors], topn = 5)
    most_similar_list_all = [x[0] for x in most_similar_all]
    most_similar_score_all = [x[1] for x in most_similar_all]

    all_dict = {}
    for i in most_similar_list_all:
        all_dict[i] = df.iloc[i].to_dict()
    return all_dict




if __name__ == "__main__":
    input_ingred = ["chicken", "potato", "spinach"]
    input_tags = ["dinner", "easy"]
    df_path = os.path.join("../test_data/kaggle_recipes", "r_cleaned_recipes_3.pkl")
    model_path = os.path.join("../../nlp_models", "nlp_model_cit.model")
    input_to_recipes_df(input_ingred, input_tags, df_path, model_path)
