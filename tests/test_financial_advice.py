import pandas as pd
import pytest
from scripts.financial_advice import generate_personalized_advice

def test_generate_personalized_advice(mocker):
    mock_df = pd.DataFrame({
        'Description': ['Rent', 'Groceries'],
        'Amount': [1000, 200],
        'Income/Expense': ['Expense', 'Expense']
    })
    mock_completion = mocker.Mock()
    mock_completion.choices[0].message.content = "This is a mock financial advice."
    mocker.patch('openai.ChatCompletion.create', return_value=mock_completion)

    result = generate_personalized_advice(mock_df, age=30, lifestyle="Urban", hobbies="Reading")
    assert isinstance(result, str)
    assert "This is a mock financial advice." in result
