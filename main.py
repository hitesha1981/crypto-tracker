import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv 

load_dotenv() 

# Use environment variable for API Key
# It will check OS env first (GitHub Actions secret), then .env file (local)
API_KEY = os.environ.get("CGK_API_DEMO_KEY")
if not API_KEY:
    raise ValueError("CGK_API_DEMO_KEY not found in environment variables or .env file.")

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
HEADERS = {}
PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 250,
    'page': 1,
    'sparkline': False,
    'price_change_percentage': '24h',
    'x-cg-demo-api-key': API_KEY
}

def fetch_crypto_data():
    """Fetches market data from CoinGecko API using API key header."""
    response = requests.get(API_URL, params=PARAMS, headers=HEADERS) 
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

def process_data(data):
    """Processes data to find top gainers, losers, and by volume."""
    df = pd.DataFrame(data)
    df = df[['symbol', 'name', 'price_change_percentage_24h', 'total_volume', 'current_price']]
    df = df.dropna()

    # 1. Top 5 Gainers (past 24 hrs)
    top_gainers = df.sort_values(by='price_change_percentage_24h', ascending=False).head(5)

    # 2. Top 5 Losers (past 24 hrs)
    top_losers = df.sort_values(by='price_change_percentage_24h', ascending=True).head(5)

    # 3. Top 5 by Trade Volume (past 24 hrs)
    top_volume = df.sort_values(by='total_volume', ascending=False).head(5)

    return top_gainers, top_losers, top_volume

def generate_markdown_table(df, title):
    """Generates a markdown table from a pandas DataFrame."""
    table = f"**{title}**\n\n"
    table += "| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |\n"
    table += "| :--: | :--: | :------------------: | :----------: | :-----------------: |\n"
    for rank, row in enumerate(df.itertuples(), 1):
        table += f"| {rank} | {row.symbol} | {row.price_change_percentage_24h:.2f}% | ${row.total_volume:,.0f} | ${row.current_price:,.4f} |\n"
    return table + "\n"

def generate_plot(gainers, losers):
    """Generates and saves a matplotlib bar chart."""
    movers = pd.concat([gainers, losers])
    movers = movers.sort_values(by='price_change_percentage_24h', ascending=True) 
    plt.figure(figsize=(10, 6))
    colors = ['green' if p > 0 else 'red' for p in movers['price_change_percentage_24h']]
    plt.barh(movers['symbol'], movers['price_change_percentage_24h'], color=colors)
    plt.xlabel('Percentage Change (24h %)')
    plt.title('Top 5 Gainers and Losers (24h)')
    plt.gca().invert_yaxis() 
    plt.tight_layout()
    plt.savefig('crypto_movers_plot.png')

def update_readme(tables, plot_path='crypto_movers_plot.png'):
    """Updates the README.md file with new data, preserving content before and after markers."""
    readme_path = 'README.md'   
    # Define the markers
    start_marker = "<!-- START_DYNAMIC_CONTENT -->"
    end_marker = "<!-- END_DYNAMIC_CONTENT -->"
    
    # Initialize variables for content parts
    pre_content = ""
    post_content = ""

    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extract content before the start marker
            if start_marker in content:
                pre_content = content.split(start_marker)[0].strip()
            
            # Extract content after the end marker
            if end_marker in content:
                # Find the position of the end marker and slice everything after it
                end_pos = content.find(end_marker) + len(end_marker)
                post_content = content[end_pos:].strip()

    # Build the new content block
    new_dynamic_content = f"\nLast updated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M UTC')}\n\n"
    
    # Add plot reference
    if os.path.exists(plot_path):
        new_dynamic_content += f"![Crypto Movers Plot]({plot_path})\n\n"

    # Add tables
    for table in tables:
        new_dynamic_content += table
        new_dynamic_content += "\n"

    # Assemble the final README content
    final_readme_content = f"{pre_content}\n\n{start_marker}{new_dynamic_content}{end_marker}\n\n{post_content}"

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(final_readme_content.strip() + "\n")


if __name__ == "__main__":
    try:
        data = fetch_crypto_data()
        gainers, losers, volume = process_data(data)
        # Generate tables
        gainers_table = generate_markdown_table(gainers, "🚀 Top 5 Gainers (24h)")
        losers_table = generate_markdown_table(losers, "👇 Top 5 Losers (24h)")
        volume_table = generate_markdown_table(volume, "💎 Top 5 by Trade Volume (24h)")       
        # Generate plot
        generate_plot(gainers, losers)
        # Update README
        update_readme([gainers_table, losers_table, volume_table])
        print("README.md updated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")