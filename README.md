# Customer Support Agent

This project implements a customer support chatbot with order management capabilities. The chatbot allows customers to:

- View existing orders
- Query Info about business performing RAG
- Create new orders and update the relevant databases

Here's an overview of the customer and systems interaction flow:

![Blank diagram (15)](https://github.com/HarshJa1n/langgraph-support-poc/blob/main/assests/flow.png?raw=true)
[Watch Demo](https://www.loom.com/share/5690395a0bcf45a38ef189f1b5d0d35d?sid=c8508c56-3335-49d1-9941-65cd4e2f0c78)


## Setup

To set up the Python environment:

```bash
conda create -p ./.conda python=3.11
pip install -r requirements.txt
```

Activate the environment with:
```bash
conda activate ./.conda
```

To run the frontend:

```bash
streamlit run streamlit_frontend.py
```
