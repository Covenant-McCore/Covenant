import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

file_path = 'C:/Users/PROGRESSIVE/3D Objects/PRACTICE/africa_food_prices.csv'

@st.cache_data
def get_data():
    import warnings
    warnings.filterwarnings("ignore", category=UserWarning, module='pandas')
    
    global file_path
    df = pd.read_csv(file_path)
    return df

# Streamlit App
st.title("Africa Food Prices")
st.write("##### Historical Food Prices")

df = get_data()

# Multiselect for selecting countries for Chart 1
selected_countries_1 = st.multiselect(
    "Choose countries for Chart 1", 
    ["All"] + list(df['Country'].unique()), 
    ["All"]
)
df_filtered_1 = df.copy() if "All" in selected_countries_1 else df[df['Country'].isin(selected_countries_1)]

def plot_1(df_filtered):
    try:
        st.subheader("Top 5 Produce per Retail Market_type")
        st.text("This chart shows the top 5 produce items in the Retail market type.")
        Retail_group = df_filtered.groupby("Market_type").get_group("Retail")
        Produce_counts = Retail_group["Produce"].value_counts().head()
        fig1, ax1 = plt.subplots()
        Produce_counts.plot(kind="bar", ax=ax1)
        ax1.set_xlabel("Produce Items")
        ax1.set_ylabel("No. of Produce Items")
        st.pyplot(fig1)

    except Exception as e1:
        st.error(f"Select at least one country: {str(e1)}")

plot_1(df_filtered_1)

# Multiselect for selecting countries for Chart 2
selected_countries_2 = st.multiselect(
    "Choose countries for Chart 2", 
    ["All"] + list(df['Country'].unique()), 
    ["All"]
)
df_filtered_2 = df.copy() if "All" in selected_countries_2 else df[df['Country'].isin(selected_countries_2)]

def plot_2(df_filtered):
    try:
        st.subheader("Top 10 Countries with Highest Number of Produce Items")
        st.text("This chart shows the top 10 countries which produced the most food items in Africa.")
        Country_produce_counts = df_filtered.groupby("Country")["Produce"].count()
        Top_countries = Country_produce_counts.nlargest(10)
        fig2, ax2 = plt.subplots()
        Top_countries.plot(kind="bar", ax=ax2)
        ax2.set_xlabel("Country")
        ax2.set_ylabel("Number of Produce Items")
        st.pyplot(fig2)

    except Exception as e2:
        st.error(f"Select at least one country: {str(e2)}")

plot_2(df_filtered_2)

# Multiselect for selecting countries for Chart 3
selected_countries_3 = st.multiselect(
    "Choose countries for Chart 3", 
    ["All"] + list(df['Country'].unique()), 
    ["All"]
)
df_filtered_3 = df.copy() if "All" in selected_countries_3 else df[df['Country'].isin(selected_countries_3)]

def plot_3(df_filtered):
    try:
        st.subheader("Top 10 Countries and Years with Highest Number of Produce Items")
        st.text("This chart shows the top 10 countries which produce the most food items per year.")
        country_year_produce_counts = df_filtered.groupby(["Country", "Year"])["Produce"].count()
        top_years = country_year_produce_counts.groupby("Year").sum().nlargest(10).index
        top_countries = country_year_produce_counts.groupby("Country").sum().nlargest(10).index
        top_countries_counts = country_year_produce_counts.loc(axis=0)[top_countries, top_years]
        fig3, ax3 = plt.subplots(figsize=(12, 8))
        for country, data in top_countries_counts.groupby("Country"):
            ax3.scatter(data.index.get_level_values("Year"), data.values, label=country, alpha=0.7)
        ax3.set_xlabel("Year")
        ax3.set_ylabel("Number of Produce Items")
        ax3.set_title("Top 10 Countries and Years with Highest Number of Produce Items")
        ax3.legend()
        st.pyplot(fig3)

    except Exception as e3:
        st.error(f"Select at least one country: {str(e3)}")

plot_3(df_filtered_3)

# Multiselect for selecting countries for Chart 4
selected_countries_4 = st.multiselect(
    "Choose countries for Chart 4", 
    ["All"] + list(df['Country'].unique()), 
    ["All"]
)
df_filtered_4 = df.copy() if "All" in selected_countries_4 else df[df['Country'].isin(selected_countries_4)]

def plot_4(df_filtered):
    try:
        st.subheader("Most Produced Item per Country")
        st.text("This chart shows the food item that has the most countries producing it.")
        top_produce_per_country = df_filtered.groupby("Country")["Produce"].agg(lambda x: x.value_counts().idxmax())
        top_produce_counts = top_produce_per_country.value_counts()
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        top_produce_counts.plot(kind="bar", ax=ax4)
        ax4.set_xlabel("Produce Item")
        ax4.set_ylabel("Number of Countries")
        ax4.set_title("Most Produced Item per Country")
        st.pyplot(fig4)

    except Exception as e4:
        st.error(f"Select at least one country: {str(e4)}")

plot_4(df_filtered_4)

# Multiselect for selecting market_type for Chart 5
selected_market_type = st.multiselect(
    "Choose Market type", list(df['Market_type'].unique()), ["Retail"]
)
df_filtered_5 = df.copy() if "All" in selected_market_type else df[df['Market_type'].isin(selected_market_type)]

def plot_5(df_filtered):
    try:
        st.subheader("Top 5 Produce per Market_type")
        st.text("This chart shows the top 5 food items produced per market type.")
        top_produce_per_market_type = df_filtered.groupby("Market_type")
        produce_counts = top_produce_per_market_type["Produce"].value_counts().head(5)
        fig5, ax5 = plt.subplots()
        produce_counts.plot(kind="bar", ax=ax5)
        ax5.set_xlabel("Market Type")
        ax5.set_ylabel("No. of Produce Items")
        st.pyplot(fig5)

    except Exception as e5:
        st.error(f"Select at least one Market type: {str(e5)}")

plot_5(df_filtered_5)
