# seminars/views.py
import uuid
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Application, Seminar


def seminar_list(request):
    seminars = Seminar.objects.all()
    return render(request, "seminars/seminar_list.html", {"seminars": seminars})


def seminar_detail(request, pk):
    seminar = get_object_or_404(Seminar, pk=pk)
    return render(request, "seminars/seminar_detail.html", {"seminar": seminar})


@login_required
def apply_seminar(request, pk):
    seminar = get_object_or_404(Seminar, pk=pk)
    app = Application.objects.create(
        user=request.user, seminar=seminar, status="pending"
    )
    print(app)
    # send_mail(
    #     "セミナー申込完了",
    #     f"あなたはセミナー「{seminar.title}」に申し込みました。",
    #     "your-email@example.com",
    #     [request.user.email],
    #     fail_silently=False,
    # )

    return redirect("seminar_list")
