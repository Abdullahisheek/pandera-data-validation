# Pandera Data Validation

Detta projekt är en fördjupningsuppgift i Python för Data Science.

Syftet är att undersöka hur Python-biblioteket Pandera kan användas för att validera data och upptäcka vanliga datakvalitetsproblem.

## Funktion

Programmet läser in CSV-filer med Pandas och använder Pandera för att kontrollera att datan följer ett antal regler.

Programmet kontrollerar bland annat:

- Att ålder ligger mellan 0 och 100.
- Att lön inte är negativ.
- Att obligatoriska värden inte saknas.
- Att korrekt data kan godkännas.

## Testdata

Projektet innehåller två CSV-filer:

- `valid_data.csv` innehåller korrekt data.
- `invalid_data.csv` innehåller medvetet felaktig data för att testa valideringen.

Den felaktiga datan innehåller exempelvis:

- Negativ ålder.
- Ålder över 100.
- Saknad lön.
- Negativ lön.

## Tekniker

- Python
- Pandas
- Pandera

## Installation

Installera projektets bibliotek med:

```bash
pip install -r requirements.txt

## Kör programmet

```bash
python main.py