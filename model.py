import streamlit as st
import requests
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import random
import networkx as nx
import matplotlib.pyplot as plt


def create_book_graph(books):
    G = nx.Graph()
    for book in books:
        G.add_node(book['title'], authors=book.get('authors', ['N/A']))
    
    
    for i in range(len(books)):
        for j in range(i + 1, len(books)):
            similarity_score = compute_similarity(books[i]['title'], books[j]['title'])
            G.add_edge(books[i]['title'], books[j]['title'], weight=similarity_score)


    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title('Book Similarity Graph')

    
    return plt.gcf()

def compute_similarity(title1, title2):
    
    return random.uniform(0.5, 1.0)


def get_top_books(genre, max_results=100):
    url = f"https://openlibrary.org/subjects/{genre}.json?limit={max_results}"
    response = requests.get(url)
    if response.status_code == 200:
        books = response.json().get('works', [])
        return books
    else:
        st.error(f"Error: {response.status_code}")
        return []


def filter_top_books(books, top_n=10):
    return random.sample(books, min(len(books), top_n))


def main():
    st.title("Book Recommendation System with Graph Visualization")
    genre = st.text_input("Please enter the genre:")

    if st.button("Get Recommendation"):
        top_100_books = get_top_books(genre)
        if not top_100_books:
            st.error("No books found for the specified genre.")
            return

        top_10_books = filter_top_books(top_100_books)
        st.write("Top 10 books in the genre:")
        for idx, book in enumerate(top_10_books, 1):
            title = book['title']
            authors = ', '.join(author['name'] for author in book.get('authors', [])) if 'authors' in book else 'N/A'
            st.write(f"{idx}. {title} by {authors}")


        fig = create_book_graph(top_10_books)
        st.pyplot(fig)

if __name__ == "__main__":
    main()
