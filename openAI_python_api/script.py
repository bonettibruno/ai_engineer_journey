from openai import OpenAI

client = OpenAI()

user_profile = {}

user_profile["dietary_restrictions"] = "vegetarian, gluten-free, prefer organic ingredients, avoid processed foods"
user_profile["cuisine_preferences"] = "Italian, Mediterranean, Asian"
user_profile["ingredients_available"] = "tomatoes, spinach, mushrooms, bell peppers, onions, garlic, olive oil, pasta, rice, quinoa, tofu, chickpeas"

system_prompt = {
    "role": "system",
    "content": "Generate HTML code for a recipe blog that takes into account the user's dietary restrictions, cuisine preferences, and available ingredients."
}

user_content1 = "I want to create a recipe blog post. Here are my dietary restrictions: " + user_profile["dietary_restrictions"] + ". My cuisine preferences include: " + user_profile["cuisine_preferences"] + ". The ingredients I have available are: " + user_profile["ingredients_available"] + "."

user_content2 = "Please provide a blog post with a title, description, ingredients, and instructions. Format the ingredients and instructions as follows: Ingredients should be bulleted, and instructions should be numbered."

user_content3 = "The recipe must use only the listed ingredients and should result in a single blog post with instructions not exceeding six steps."

user_prompt = {
    "role": "user",
    "content": user_content1 + "\n" + user_content2 + "\n" + user_content3
}

response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[system_prompt, user_prompt]
)

print(response.choices[0].message.content)



# The code above ran successfully in the course page, and the output was a complete HTML code for a recipe blog post that meets the specified requirements.
# ```html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Vegetarian Mediterranean Stir-Fry with Quinoa</title>
#     <meta name="description" content="A healthy, gluten-free, vegetarian Mediterranean stir-fry using only organic, whole ingredients you have!">
#     <style>
#         body { font-family: 'Helvetica', Arial, sans-serif; max-width: 700px; margin: 2em auto; background: #faf7f5; color: #333; }
#         h2 { color: #3f7d3b; }
#         ul { margin-top: 0; }
#         ol { margin-top: 0; }
#         .ingredients, .instructions { margin-bottom: 2em; }
#         .blog-description { font-style: italic; margin-bottom: 1.5em; }
#     </style>
# </head>
# <body>
#     <h1>Vegetarian Mediterranean Stir-Fry with Quinoa</h1>
#     <div class="blog-description">
#         Looking for a quick, wholesome, and flavorful meal honoring your vegetarian, gluten-free lifestyle? This Mediterranean-inspired stir-fry features organic veggies, protein-rich tofu and chickpeas, and nutrient-dense quinoa. It’s free of processed foods and packs in the freshness of tomatoes, bell peppers, onions, and spinach—all ingredients you already have!
#     </div>
#     <h2>Ingredients</h2>
#     <ul class="ingredients">
#         <li>1 cup quinoa (uncooked)</li>
#         <li>2 cups water</li>
#         <li>2 tablespoons olive oil</li>
#         <li>1 cup cherry tomatoes, halved (or chopped tomatoes)</li>
#         <li>1 cup spinach, roughly chopped</li>
#         <li>1 cup mushrooms, sliced</li>
#         <li>1 bell pepper, diced</li>
#         <li>1 small onion, diced</li>
#         <li>2 garlic cloves, minced</li>
#         <li>200g tofu, cubed</li>
#         <li>1 cup cooked chickpeas</li>
#         <li>Salt and pepper, to taste</li>
#     </ul>
#     <h2>Instructions</h2>
#     <ol class="instructions">
#         <li>Rinse quinoa and bring to a boil with water in a saucepan. Reduce heat, cover, and simmer for 12–15 minutes until water is absorbed. Fluff and set aside.</li>
#         <li>While quinoa cooks, heat olive oil in a large skillet over medium heat. Sauté onions and garlic for 2–3 minutes until soft.</li>
#         <li>Add mushrooms, bell pepper, and tofu to the skillet. Cook 4–5 minutes, stirring occasionally, until veggies are tender and tofu is golden.</li>
#         <li>Stir in tomatoes, spinach, and chickpeas. Cook another 2–3 minutes until spinach wilts and tomatoes soften.</li>
#         <li>Add the cooked quinoa to the skillet. Toss well to combine. Season with salt and pepper to taste.</li>
#         <li>Serve warm and enjoy your nourishing Mediterranean stir-fry, perfect for a vegetarian, gluten-free diet!</li>
#     </ol>
# </body>
# </html>
# ```