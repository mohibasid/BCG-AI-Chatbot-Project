
def simple_chatbot(user_query):
    if user_query == "What was the total revenue for Microsoft in 2022 ?":
        return "The total revenue is $198.27 million."
    elif user_query == "How has net income of Microsoft changed from 2022 to 2023?":
        return "The net income has decreased by -0.51% from 2022 to 2023"
    elif user_query == "What were the total assets for Microsoft in 2024?":
        return "The total expenses are $512.163 million."
    elif user_query == "What was the revenue growth of Microsoft from 2023 to 2024?":
        return "The revenue growth from 2023 to 2024 was 15.66%."
    elif user_query == "What is the change in total assets for Microsoft from 2023 to 2024?":
        return "The change in total assets from 2023 to 2024 is 24.31% "
    else:
        return "Sorry, I can only provide information on predefined queries."

# Simulated command-line interaction (works in Colab)
user_input = input("Ask a financial question (or type 'exit' to quit): ")
while user_input.lower() != 'exit':
    print(simple_chatbot(user_input))
    user_input = input("Ask another question: ")
