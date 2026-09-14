# Quant Analyzer (Financial Visualization Suite)

A standalone Python quantitative analysis engine designed to transform raw OHLCV market data into institutional-grade financial metrics and interactive visualizations. Built with Pandas and Plotly, this tool helps traders and analysts visualize risk, reward, and market structure.

## Overview
This script ingests clean historical market data, computes advanced statistical metrics, and generates a suite of interactive, browser-based dashboards. It is currently optimized for cryptocurrency assets (utilizing a 365-day trading year for volatility calculations) but can be easily adapted for traditional equities.

## Core Metrics Calculated
* **Moving Averages:** 20-day and 50-day Simple Moving Averages (SMA) for trend identification.
* **Logarithmic Returns:** Symmetrical continuous growth measurement using $R_{log} = \ln(P_t / P_{t-1})$.
* **Annualized Volatility:** 30-day rolling risk profile scaled for 24/7 crypto markets using $\sigma_{annual} = \sigma_{daily} \times \sqrt{365}$.
* **Maximum Drawdown:** Peak-to-trough drop measuring investor pain using $D = \frac{V - P}{P}$.

## Visualization Engine
The suite automatically generates three interactive Plotly canvases:
* **Price Action Canvas:** A dynamic candlestick chart overlaid with 20-day and 50-day SMAs.
* **The Quant Tearsheet:** A 3-story synchronized dashboard comparing Cumulative Return (reward), Rolling Volatility (risk), and an "underwater" area chart mapping Max Drawdown.
* **Returns Distribution:** A 100-bin histogram of log returns to visualize market behavior and identify unpredictable "fat tail" events.

## Setup & Usage
1. **Install Dependencies:** Run `pip install pandas numpy plotly` in your terminal.
2. **Execute Script:** Run the Python script in the same directory as your target CSV file.
3. **Input Filename:** Enter the exact name of your data file (e.g., `BTC-USD.csv`) when prompted. The charts will automatically render and open in your default web browser.