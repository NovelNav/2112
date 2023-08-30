from django.contrib.auth.decorators import login_required
from .models import Student, Librarian

@login_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    borrow_records = BorrowRecord.objects.filter(student=student)
    return render(request, 'library_app/student_dashboard.html', {'borrow_records': borrow_records})

@login_required
def librarian_dashboard(request):
    if request.user.is_staff:
        librarian = Librarian.objects.get(user=request.user)
        borrow_records = BorrowRecord.objects.all()
        return render(request, 'library_app/librarian_dashboard.html', {'borrow_records': borrow_records})
    else:
        return HttpResponse("You don't have librarian privileges.")
