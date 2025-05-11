[![Books Recommendation System | Books ...](https://images.openai.com/thumbnails/3ddebcdc364b53a40895dfe2599e3c93.png)](https://pritamaich.github.io/Books-Recommendation-System/)

---

# 📚 AI-Powered Book Recommender System

An intelligent, genre-based book recommendation application built with **Streamlit**, leveraging **transformer-based NLP models**, **graph analytics**, and real-time data from the **Open Library API**. This system combines **Natural Language Processing (NLP)**, **automated summarization**, and **network visualization** to provide personalized and insightful book recommendations.

---

## 🚀 Key Features

### 🔍 Genre-Based Book Discovery

* **User Input**: Enter a genre (e.g., "science fiction", "mystery").
* **Data Retrieval**: Fetches top books in the specified genre using the Open Library API.

### 🧠 AI-Powered Summarization

* **Transformer Models**: Utilizes pre-trained transformer models (e.g., BART, T5) from Hugging Face to generate concise summaries of book descriptions.
* **Enhanced Understanding**: Summaries provide quick insights into each book's content, aiding in informed decision-making.

### 📊 Graph-Based Visualization

* **NetworkX Integration**: Constructs a graph where nodes represent books and edges indicate relationships (e.g., shared authors, similar themes).
* **Matplotlib Rendering**: Visualizes the graph to illustrate connections between recommended books, enhancing exploration.

---

## 🧠 Underlying Technologies

* **Natural Language Processing**: Employs transformer-based models for text summarization, capturing contextual nuances in book descriptions.
* **Graph Theory**: Applies concepts from graph theory to model and visualize relationships between books.
* **Data Visualization**: Uses Matplotlib to render interactive graphs, facilitating user engagement and exploration.

---

## 🛠️ Installation & Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/VanshGupta-2404/Book_recommendation.git
   cd Book_recommendation
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:

   ```bash
   streamlit run app.py
   ```

---

## 🧪 Customization Options

* **Model Selection**: Swap out the transformer model in `summarizer.py` to experiment with different summarization techniques.
* **Graph Parameters**: Adjust graph construction parameters in `graph_builder.py` to explore various relationship mappings.
* **UI Enhancements**: Modify `app.py` to customize the Streamlit interface, adding features like user ratings or filters.

---

## 🔐 Security Considerations

* **API Keys**: Ensure that any API keys (e.g., for Open Library) are stored securely, using environment variables or configuration files excluded from version control.
* **Data Privacy**: If integrating user data, comply with data protection regulations and best practices.

---

## 📫 Contact

For questions, feedback, or collaboration opportunities:

* **Email**: [guptavansh2404@gmail.com](mailto:guptavansh2404@gmail.com)
* **GitHub**: [VanshGupta-2404](https://github.com/VanshGupta-2404)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---
