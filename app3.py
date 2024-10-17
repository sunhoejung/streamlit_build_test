# -*- utf-8 -*-

import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import yfinance as yf

def main():
    with st.sidebar:
        st.title("Stock Chart")

    