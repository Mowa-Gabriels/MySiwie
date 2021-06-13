from django.shortcuts import render, HttpResponseRedirect,redirect
from .models import Internship, Logbook
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .form import ProfileForm, UserForm, LogForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages



# Create your views here.



@login_required()
def Index(request):
      internship = Internship.objects.all()[3:]

      context = {'internship': internship}
      return render(request, 'index.html', context)

@login_required()
def Employers_list(request):
    internship = Internship.objects.all().order_by('-name_of_org')

    context = {'internship': internship}
    return render(request, 'employers_listpage.html', context)

def search(request):
    internship = Internship.objects.all()

    keyword = request.GET.get("keyword")
    city = request.GET.get("city")

    if keyword and city:
        query_set = internship.filter(
            Q(name_of_org__icontains=keyword) |
            Q(address__icontains=city) |
            Q(state__name__icontains= city) |
            Q(course__name__icontains=keyword)
        ).distinct()

        count = internship.filter(
            Q(name_of_org__icontains=keyword) |
            Q(address__icontains=city) |
            Q(state__name__icontains=city) |
            Q(course__name__icontains=keyword)
        ).count()

    elif keyword:
        query_set = internship.filter(
            Q(name_of_org__icontains=keyword) |
            Q(address__icontains=keyword) |
            Q(state__name__icontains=keyword) |
            Q(course__name__icontains=keyword)
        ).distinct()
        count = internship.filter(
            Q(name_of_org__icontains=keyword) |
            Q(address__icontains=keyword) |
            Q(state__name__icontains=keyword) |
            Q(course__name__icontains=keyword)
        ).count()

    elif city:
        query_set = internship.filter(

            Q(address__icontains=city) |
            Q(state__name__icontains=city)

        ).distinct()

        count = internship.filter(

            Q(address__icontains=city) |
            Q(state__name__icontains=city)

        ).count()

    else:
        query_set = internship



    context = {'internship':internship,
               'query_set':query_set,
               'keyword':keyword,
               'city':city,
               'count': count}
    return render(request, 'search_page.html', context)


@login_required()
def Dashboard(request):
      log_user = request.user

      logbooks = Logbook.objects.filter(user = log_user)

      context = {'logbooks':logbooks}
      return render(request, 'dashboard.html', context)

@login_required()
def Profile(request):
      internship = Internship.objects.all()
      logbook = Logbook.objects.all()[15:]

      context = {'internship':internship,
                 'logbook':logbook}
      return render(request, 'profile.html', context)

@login_required()
def ProfileEdit(request):

      context = {}
      return render(request, 'profile-edit.html', context)


@login_required()
def Detail(request, intern_id):
    intern = Internship.objects.get(pk=intern_id)
    context = {
        'intern': intern
    }
    return render(request, 'career-single.html', context)

@login_required()
def OndoSearch(request):
    internship = Internship.objects.all()

    query_set = internship.filter(

        Q(state__name__icontains='ondo')

    ).distinct()

    count = internship.filter(

        Q(state__name__icontains='ondo')

    ).count()

    context = {'internship': internship,
               'query_set': query_set,
               'state': 'Ondo',
               'count':count}
    return render(request, 'state_searchpage.html', context)

@login_required()
def LagosSearch(request):
    internship = Internship.objects.all()

    query_set = internship.filter(

        Q(state__name__icontains='lagos')

    ).distinct()

    count = internship.filter(

        Q(state__name__icontains='lagos')

    ).count()

    context = {'internship': internship,
               'query_set': query_set,
               'state': 'Lagos',
               'count':count}
    return render(request, 'state_searchpage.html', context)

@login_required()
def AbujaSearch(request):
    internship = Internship.objects.all()

    query_set = internship.filter(

        Q(state__name__icontains='abuja')

    ).distinct()

    count = internship.filter(

        Q(state__name__icontains='abuja')

    ).count()

    context = {'internship': internship,
               'query_set': query_set,
               'state': 'Abuja',
               'count':count}
    return render(request, 'state_searchpage.html', context)

@login_required()
def OyoSearch(request):
    internship = Internship.objects.all()

    query_set = internship.filter(

        Q(state__name__icontains= 'oyo')

    ).distinct()

    count = internship.filter(

        Q(state__name__icontains='oyo')

    ).count()

    context = {'internship': internship,
               'query_set':query_set,
               'state': 'Oyo',
               'count':count}
    return render(request, 'state_searchpage.html', context)


class ProfileUpdateView(LoginRequiredMixin,TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'profile-edit.html'

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)


        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile was successfully updated')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


from django.utils import timezone
@login_required()
def Addlog(request):
    now = timezone.now()


    if request.method == 'POST':
        form = LogForm(request.POST)

        if form.is_valid:
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()

            return redirect('dashboard')
    else:
        form = LogForm()

    context = {
        'form': form,
        'now': now,

    }
    return render(request, 'add_log.html', context)


@login_required()
def AboutPage(request):

      context = {}
      return render(request, 'about_page.html', context)
