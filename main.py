import pandas as pd
import pandera.pandas as pa
from pandera.pandas import Column, Check, DataFrameSchema
schema = DataFrameSchema({
    "name": Column(str, nullable=False),

    "age": Column(
        int,
        Check.in_range(0, 100),
        nullable=False
    ),

    "salary": Column(
        float,
        Check.ge(0),
        nullable=False,
        coerce=True
    )
})
def validate_data(file_path):
    df = pd.read_csv(file_path)

    print("\nData som kontrolleras:")
    print(df)

    try:
        schema.validate(df, lazy=True)

        print("\nData är godkänd!")

    except pa.errors.SchemaErrors as error:
        print("\nData innehåller valideringsfel:")

        print(
            error.failure_cases[
                ["column", "failure_case", "check"]
            ]
        )

print("TEST 1 - KORREKT DATA")

validate_data("data/valid_data.csv")

print("\nTEST 2 - FELAKTIG DATA")

validate_data("data/invalid_data.csv")