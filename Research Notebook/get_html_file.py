import pandas as pd
from IPython.display import HTML, display
import os  # Added to handle directory creation

# Read the CSV file (adjust path to your Complete.csv location)
try:
    df = pd.read_csv(r"..\data\Complete.csv", index_col=False, encoding='unicode_escape')
    videos_per_page = 10  # 10 videos per page
    num_pages = (len(df) + videos_per_page - 1) // videos_per_page  # Calculate total pages (e.g., 40 / 10 = 4)

    # Ensure the frontend directory exists
    frontend_path = r"..\frontend"
    os.makedirs(frontend_path, exist_ok=True)  # Creates directory if it doesn't exist

    # Generate HTML for each page
    for page in range(num_pages):
        html = ""
        start_idx = page * videos_per_page
        end_idx = min((page + 1) * videos_per_page, len(df))
        page_videos = df[start_idx:end_idx]

        # Generate recipe cards for this page
        for index, row in page_videos.iterrows():
            public_url = row.get("Public URL", "")
            video_id = public_url.split("/d/")[1].split("/")[0] if pd.notna(public_url) and "drive.google.com" in public_url else ""
            title = row.get("Title", row.get("title", ""))
            description = row.get("Recipe in Plain text", row.get("description", ""))

            if video_id and title:
                html += '<div class="recipe-card">\n'
                html += f'    <iframe src="https://drive.google.com/file/d/{video_id}/preview" allow="autoplay" loading="lazy"></iframe>\n'
                html += f'    <h3>{title}</h3>\n'
                html += f'    <p>{description if pd.notna(description) else "No description available"}</p>\n'
                html += '</div>\n'
            else:
                print(f"Skipping row {index} due to missing video_id or title. Public URL: {public_url}, Title: {title}")

        # Wrap in full HTML structure
        full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shared Skillet | Recipes - Page {page + 1}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Poppins', sans-serif;
            background: #f9f9f9;
            color: #333;
            line-height: 1.6;
            min-height: 100vh;
        }}
        header {{
            background: rgba(0, 0, 0, 0.8);
            padding: 10px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 10;
        }}
        header .logo img {{
            height: 40px;
        }}
        nav ul {{ list-style: none; display: flex; gap: 15px; }}
        nav a {{ color: #fff; text-decoration: none; font-weight: 500; font-size: 0.9em; transition: color 0.3s; }}
        nav a:hover {{ color: #e67e22; }}
        .search-bar {{
            padding: 20px;
            text-align: center;
            margin-top: 60px;
        }}
        .search-bar input {{
            padding: 10px;
            width: 80%;
            max-width: 500px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 1em;
        }}
        .recipes-section {{
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
            margin-top: 100px;
        }}
        .recipes-section h2 {{
            font-size: 2em;
            color: #e67e22;
            text-align: center;
            margin-bottom: 20px;
        }}
        .recipe-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }}
        .recipe-card {{
            background: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            transition: transform 0.3s;
        }}
        .recipe-card:hover {{ transform: translateY(-5px); }}
        .recipe-card iframe {{
            width: 100%;
            height: 50vw;
            max-height: 200px;
            min-height: 150px;
            border: none;
        }}
        .recipe-card h3 {{
            font-size: 1.3em;
            color: #333;
            padding: 10px;
        }}
        .recipe-card p {{
            padding: 0 10px 10px;
            font-size: 0.9em;
            color: #666;
            overflow-wrap: break-word;
            max-height: 100px;
            overflow-y: auto;
        }}
        .pagination {{
            text-align: center;
            margin: 20px 0;
        }}
        .pagination a {{
            color: #e67e22;
            text-decoration: none;
            padding: 5px 10px;
            margin: 0 5px;
            border: 1px solid #e67e22;
            border-radius: 5px;
        }}
        .pagination a:hover {{ background: #e67e22; color: #fff; }}
        footer {{
            background: rgba(0, 0, 0, 0.8);
            padding: 10px;
            text-align: center;
            font-size: 0.8em;
            color: #fff;
            width: 100%;
        }}
        @media (max-width: 768px) {{
            header {{ flex-direction: column; padding: 10px; }}
            header .logo img {{ height: 30px; }}
            nav ul {{ flex-direction: column; gap: 10px; text-align: center; }}
            .search-bar {{ margin-top: 80px; }}
            .recipes-section {{ padding: 10px; margin-top: 120px; }}
            .recipes-section h2 {{ font-size: 1.5em; margin-bottom: 20px; }}
            .recipe-grid {{ grid-template-columns: 1fr; gap: 15px; }}
            .recipe-card iframe {{ height: 50vw; min-height: 150px; }}
            .recipe-card h3 {{ font-size: 1.1em; }}
            .recipe-card p {{ font-size: 0.8em; max-height: 80px; }}
            footer {{ font-size: 0.7em; padding: 8px; }}
        }}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div class="logo">
            <a href="index.html"><img src="logo.png" alt="Shared Skillet Logo"></a>
        </div>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="recipes1.html">Recipes</a></li>
                <li><a href="index.html#businessPlan" onclick="showBusinessPlan()">About</a></li>
            </ul>
        </nav>
    </header>

    <div class="search-bar">
        <input type="text" id="searchInput" placeholder="Search recipes..." onkeyup="searchRecipes()">
    </div>

    <section class="recipes-section">
        <h2>Explore Our Recipes - Page {page + 1}</h2>
        <div class="recipe-grid">
            {html}
        </div>
        <div class="pagination">
'''

        # Add pagination links
        for p in range(num_pages):
            full_html += f'<a href="recipes{p + 1}.html">{p + 1}</a>'

        full_html += '''
        </div>
    </section>

    <footer>© 2025 Shared Skillet | Crafted with Love ❤️</footer>

    <script>
        function searchRecipes() {
            let input = document.getElementById("searchInput").value.toLowerCase();
            let cards = document.getElementsByClassName("recipe-card");
            for (let i = 0; i < cards.length; i++) {
                let title = cards[i].getElementsByTagName("h3")[0].innerText.toLowerCase();
                let description = cards[i].getElementsByTagName("p")[0].innerText.toLowerCase();
                if (title.includes(input) || description.includes(input)) {
                    cards[i].style.display = "";
                } else {
                    cards[i].style.display = "none";
                }
            }
        }
    </script>
</body>
</html>
'''

        # Save the page to the frontend directory
        with open(os.path.join(frontend_path, f"recipes{page + 1}.html"), "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"Generated {os.path.join(frontend_path, f'recipes{page + 1}.html')}")

except FileNotFoundError:
    print("Error: Complete.csv not found. Check the file path.")
except KeyError as e:
    print(f"Error: Column {e} not found in CSV. Check your column names.")
except Exception as e:
    print(f"An error occurred: {e}")