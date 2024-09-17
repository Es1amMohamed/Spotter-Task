from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def recommend_books(user_favorites):
    """
    Recommends books based on the user's favorite books.

    Args:
        user_favorites (QuerySet): A queryset of Favorite objects for the logged-in user.

    Returns:
        list: A list of recommended Book objects, up to 5 recommendations.
    """
    # Collect the books and their titles from the user's favorites
    books = [favorite.book for favorite in user_favorites]
    book_titles = [book.title for book in books]

    # Convert book titles to TF-IDF representation
    vectorizer = TfidfVectorizer().fit_transform(book_titles)
    cosine_similarities = linear_kernel(vectorizer, vectorizer)

    # Determine recommendations based on similarity
    recommendations = []
    for idx, book in enumerate(books):
        # Get similarity scores for the current book
        sim_scores = list(enumerate(cosine_similarities[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        # Get indices of the top 5 recommendations (excluding the book itself)
        sim_scores = sim_scores[1:6]
        book_indices = [i[0] for i in sim_scores]
        recommendations.extend([books[i] for i in book_indices])

    recommendations = list(set(recommendations))
    # Return up to 5 recommended books
    return recommendations[:5]
