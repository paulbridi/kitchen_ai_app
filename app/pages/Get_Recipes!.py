import streamlit as st
import requests

url = 'http://127.0.0.1:8003'

if 'ings' not in st.session_state:
    st.session_state['ings'] = 0

if 'prefs' not in st.session_state:
    st.session_state['prefs'] = 0

st.write(st.session_state['ings'])
st.write(st.session_state['prefs'])


# # returning ingredient names, images and preferences
# st.subheader(f"I can see ..[include CNN returned predictions here]")

# #images in lst list
# img_list = ["image1", "image2", "image3"]
# col = st.columns(len(img_list))
# for i,img in enumerate(img_list):
#     with col[i]:
#         # st.image(img)
#         st.write(img)

# st.subheader(f"Your preferences are ...")

# dummy response --> delete once packaged
response = {'suggest_recipes': {'119527': {'Name': "Rick's Lemon Chicken", \
                'RecipeCategory': 'Whole Chicken', 'Calories': 632.6, \
                'images': ['Not Provided'], 'cook_time': '1 Hour(s) 30 Minute(s) ',\
                'prep_time': '15 Minute(s) ', 'total_time': '1 Hour(s) 45 Minute(s) ',\
                'recipe_servings': 6, 'tags': ['chicken', 'poultry', 'meat', '< 4 hours', 'easy'], \
                'instructions': ['Preheat oven to 375°f.', 'Place chicken and potatoes in baking pan.',\
                'Top with lemon juice and butter.', 'Salt and pepper.', \
                    'Bake uncovered for 1 to 1 1/2 hour or until potatoes are fork tender and chicken runs clear.'],\
                'ingredient_quantities': ['4 1/4', '5', '4', 'na', 'na', '1/4'],\
                'ingredients': ['chicken', 'potatoes', 'salt', 'fresh ground black pepper', 'butter'],\
                'ingredients_cleaned': ['chicken', 'potato'],\
                'ingred_and_tags': ['chicken', 'potato', 'chicken', 'poultry', 'meat', '< 4 hours', 'easy'],\
                'name_cat_ingred_tag': ["Rick's", 'Lemon', 'Chicken', 'Whole', 'Chicken', 'chicken', 'potato', 'chicken', 'poultry', 'meat', '< 4 hours', 'easy'],\
                'cat_ingred_tag': ['Whole', 'Chicken', 'chicken', 'potato', 'chicken', 'poultry', 'meat', '< 4 hours', 'easy']}, '312221': {'Name': 'Pasty', 'RecipeCategory': 'Savory Pies', 'Calories': 799.7, 'images': ['https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/32/41/69/pic9kkmtu.jpg', 'https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/32/41/69/picpa3gyj.jpg', 'https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/32/41/69/picsqny8p.jpg', 'https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/32/41/69/picw5i8sm.jpg'], 'cook_time': '1 Hour(s) ', 'prep_time': '45 Minute(s) ', 'total_time': '1 Hour(s) 45 Minute(s) ', 'recipe_servings': 12, 'tags': ['< 4 hours'], 'instructions': ['Preheat over to 350 degrees.', 'Thaw pie crust dough and warm to room temperature.', 'Mix vegetables.', 'Meat and seasoning in a large bowl.', 'Roll each pie crust into a 10 inch oval.', 'Put 10 oz pasty filling on each dough sheet.', 'Pull over the top and crimp the edges.', 'Bake for 1 hour at 350 degrees.', 'Serve with or without your favorite gravy.'], 'ingredient_quantities': ['3', '1', '2', '2', '2', 'na', '48', 'na'], 'ingredients': ['potatoes', 'carrot', 'onions', 'chicken'], 'ingredients_cleaned': ['potato', 'carrot', 'chicken'], 'ingred_and_tags': ['potato', 'carrot', 'chicken', '< 4 hours'], 'name_cat_ingred_tag': ['Pasty', 'Savory', 'Pies', 'potato', 'carrot', 'chicken', '< 4 hours'], 'cat_ingred_tag': ['Savory', 'Pies', 'potato', 'carrot', 'chicken', '< 4 hours']}, '452116': {'Name': 'Chicken and Vegetable Hotpot', 'RecipeCategory': 'Chicken', 'Calories': 364.7, 'images': ['Not Provided'], 'cook_time': '1 Hour(s) 15 Minute(s) ', 'prep_time': '10 Minute(s) ', 'total_time': '1 Hour(s) 25 Minute(s) ', 'recipe_servings': 4, 'tags': ['poultry', 'meat', '< 4 hours', 'easy'], 'instructions': ['Place the chicken.', 'Vegetables.', 'And soup mix into a large pan with 600ml water.', 'Stir well; bring to a boil; and simmer for 10 minutes.', 'Meanwhile.', 'Cook the potato slices in a pan of lightly salted water for 5 minutes; drain.', 'Preheat the oven to 350 degrees fahrenheit/180 degrees celsius/gas 4.', 'Spoon the chicken mixture into a casserole dish.', 'Arrange the potato slices over the top.', 'Brush with the melted butter.', 'Bake for 1 hour until the potatoes are golden.'], 'ingredient_quantities': ['400', '350', '60', '500', '30'], 'ingredients': ['chicken', 'potatoes', 'butter'], 'ingredients_cleaned': ['chicken', 'potato'], 'ingred_and_tags': ['chicken', 'potato', 'poultry', 'meat', '< 4 hours', 'easy'], 'name_cat_ingred_tag': ['Chicken', 'and', 'Vegetable', 'Hotpot', 'Chicken', 'chicken', 'potato', 'poultry', 'meat', '< 4 hours', 'easy'], 'cat_ingred_tag': ['Chicken', 'chicken', 'potato', 'poultry', 'meat', '< 4 hours', 'easy']}, '401370': {'Name': 'Portuguese Sausage Soup', 'RecipeCategory': '< 30 Mins', 'Calories': 393.5, 'images': ['Not Provided'], 'cook_time': '20 Minute(s) ', 'prep_time': '10 Minute(s) ', 'total_time': '30 Minute(s) ', 'recipe_servings': 6, 'tags': ['null'], 'instructions': ['In a large saucepan cook all the sausage and onion until sausage is browned and onion is tender.', 'Drain fat.', 'Add the potatoes.', 'Your choice of broth.', 'Spinach.', 'Your choice of beer or water.', 'And pepper.', 'Bring to boiling;  reduce heat.', 'Cover and simmer about 20 mins or until potatoes are tender.'], 'ingredient_quantities': ['4', '4', '1/2', '2', '2', '1', '1/2', '1/4'], 'ingredients': ['sweet italian sausage links', 'onion', 'potatoes', 'chicken', 'vegetable broth', 'frozen chopped spinach', 'beer', 'water', 'pepper'], 'ingredients_cleaned': ['sweet italian sausage link', 'potato', 'chicken', 'vegetable broth', 'spinach', 'beer'], 'ingred_and_tags': ['sweet italian sausage link', 'potato', 'chicken', 'vegetable broth', 'spinach', 'beer', 'null'], 'name_cat_ingred_tag': ['Portuguese', 'Sausage', 'Soup', '<', '30', 'Mins', 'sweet italian sausage link', 'potato', 'chicken', 'vegetable broth', 'spinach', 'beer', 'null'], 'cat_ingred_tag': ['<', '30', 'Mins', 'sweet italian sausage link', 'potato', 'chicken', 'vegetable broth', 'spinach', 'beer', 'null']}, '385788': {'Name': 'Chicken, Potato and Spinach Curry', 'RecipeCategory': 'Curries', 'Calories': 182.3, 'images': ['https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/39/96/50/picwecbep.jpg'], 'cook_time': '20 Minute(s) ', 'prep_time': '10 Minute(s) ', 'total_time': '30 Minute(s) ', 'recipe_servings': 4, 'tags': ['chicken thigh & leg', 'chicken', 'poultry', 'meat', 'asian', 'indian', '< 30 mins'], 'instructions': ['Heat 2 tablespoons oil and add the onion.', 'Curry paste and the potato.', 'Stir until potato starts to brown.', 'About 5 minutes.', 'Add the stock and bring to a rapid boil.', 'Add the chicken and the spinach.', 'Reduce the heat and simmer.', 'Covered.', 'For 7 minutes.', 'Season with salt and fresh lime juice.'], 'ingredient_quantities': ['250', '2', '1', '2', '1', '1', '4', 'na', 'na'], 'ingredients': ['spinach', 'onion', 'curry paste', 'potato', 'salt', 'lime juice'], 'ingredients_cleaned': ['spinach', 'curry paste', 'potato', 'lime juice'], 'ingred_and_tags': ['spinach', 'curry paste', 'potato', 'lime juice', 'chicken thigh & leg', 'chicken', 'poultry', 'meat', 'asian', 'indian', '< 30 mins'], 'name_cat_ingred_tag': ['Chicken,', 'Potato', 'and', 'Spinach', 'Curry', 'Curries', 'spinach', 'curry paste', 'potato', 'lime juice', 'chicken thigh & leg', 'chicken', 'poultry', 'meat', 'asian', 'indian', '< 30 mins'], 'cat_ingred_tag': ['Curries', 'spinach', 'curry paste', 'potato', 'lime juice', 'chicken thigh & leg', 'chicken', 'poultry', 'meat', 'asian', 'indian', '< 30 mins']}}}

# dummy params --> delete once packaged
parameters = {"ingredients": st.session_state['ings'],
              "preferences": st.session_state['prefs']}


################### NLP MODEL FUNCTIONS ####################

# call and get response for recipes
response_recipes = requests.get(url + "/suggest_recipes", params=parameters).json()

#converting response json to readable format
def get_recipes_expand(response_recipes):
    """ Returning top 5 recipes each in an st.expander """
    index_list = list(response_recipes['suggest_recipes'].keys())

    for i, index in enumerate(index_list):
        column_names = response_recipes['suggest_recipes'][index]
        with st.expander(f"{i+1} - {column_names['Name']}"):
            st.header(f":red[{column_names['Name']}]")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Recipe ID:** {index} \n")
                # st.markdown("")
                st.markdown(f"**Serving(s):** {column_names['recipe_servings']}")
                st.markdown(f"**Calories:** {column_names['Calories']} kcal \n")
                # st.markdown("")
            with col2:
                st.markdown(f"**Cook time:** {column_names['cook_time']}")
                st.markdown(f"**Preparation time:** {column_names['prep_time']}")
                st.markdown(f"**Total time:** {column_names['total_time']}\n")
                # st.markdown("")

            st.markdown(f"#### Ingredients")
            for i, ingredient in enumerate(column_names['ingredients']):
                st.markdown(ingredient.capitalize())

            st.markdown(f"\n#### Instructions")
            for i, step in enumerate(column_names['instructions'],1):
                st.markdown(f"{i}. {step}")
            st.markdown("")

            try:
                st.image(column_names["images"][0], caption = column_names['Name'], width=300)
            except:
                st.markdown(f"**Image not provided**")


# make recipes api call button
if st.button("Let's get some recipes!"):
    st.markdown("")
    st.markdown(f"#### These are the top 5 recipes based on the ingredients and preferences you provided:")
    get_recipes_expand(response_recipes)
else:
    pass
