# Subscription Manager

A subscription manager developed in Python to help control monthly spending on subscription services.

## Features

- Add new subscriptions
- Remove existing subscriptions
- View total subscription value
- Generate Spend Chart for the Last 12 Months
- Control of monthly payments

## Technologies Used

- Python
- SQLModel
- Matplotlib
- SQLite

## Project Structure

```
Subscription Manager/
├── scr/
│   ├── models/
│   │   ├── database.py
│   │   └── model.py
│   ├── templates/
│   │   └── app.py
│   └── views/
│       └── view.py
├── venv/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## How install

1. Clone the repositore:
```bash
git clone https://github.com/seu-usuario/subscription-manager.git
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the .env file with its environment variables

5. Run the App:
```bash
python scr/template/app.py
```

## How used

1. When you launch the program, you will see a menu with the following options:
   - Add Subscription
   - Remove Subscription
   - Total Values
   - Expenses in the last 12 months
   - Exit

2. Choose the desired option by entering the corresponding number

3. Follow the on-screen instructions for each operation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is under the MIT license.
