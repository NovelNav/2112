urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('librarian/', views.librarian_dashboard, name='librarian_dashboard'),
]
