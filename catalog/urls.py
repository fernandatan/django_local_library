from django.urls import path
from . import views

# view function (index) will be called if the URL pattern ('') is detected.
# name parameter is a unique identifier for this URL mapping - can be used to reverse the mapper
# the URL must already have matched /catalog, so the view will actually be called for the URL: /catalog/books/.
# '<int:pk>' captures the book id, which must be an integer and pass it to the view as a parameter named pk (primary key), used to store the book uniquely in the database.
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]

urlpatterns += [   
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

urlpatterns += [   
    path('borrowed/', views.LoanedBooksListView.as_view(), name='all-borrowed'),
]

# redirect URLs with the format /catalog/book/<bookinstance id>/renew/ to the function named renew_book_librarian() in views.py, and send the BookInstance id as the parameter named pk.
urlpatterns += [   
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [  
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

urlpatterns += [  
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]