# Pandera Data Validation

Detta projekt är en fördjupningsuppgift i Python för Data Science.

Syftet är att lära mig grunderna i datavalidering med biblioteket Pandera.

## Vad programmet gör

Programmet läser in CSV-filer med Pandas och kontrollerar datan med Pandera.

Det kontrollerar bland annat:

- att ålder ligger mellan 0 och 100
- att lön inte är negativ
- att obligatoriska värden inte saknas

Projektet innehåller två CSV-filer:

- `valid_data.csv` med korrekt data
- `invalid_data.csv` med medvetet felaktig data

## Tekniker

- Python
- Pandas
- Pandera

## Installation

Kör detta i terminalen:

```bash
pip install -r requirements.txt
python main.py
