# Customer Support Agent

This project implements a customer support chatbot with order management capabilities. The chatbot allows customers to:

- View existing orders
- Create new orders and update the relevant databases

Here's an overview of the system architecture:

![Blank diagram (15)](https://github.com/user-attachments/assets/62305fcb-3414-41a2-9e2d-8f306219ccc0)

And here's an example of a customer interaction flow:

![image](https://github.com/user-attachments/assets/8230d153-22d4-422d-9746-afbeda7ba69c)

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