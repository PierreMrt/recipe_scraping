from django.shortcuts import render
from django.views.generic.edit import CreateView

def index(request):
    return render(request, 'base.html')

class SearchCreateView(CreateView):
    model = Search
    fields = ['job', 'country']
    template_name = 'jobs/search_form.html'
    success_url = '/'
    
    def form_valid(self, form):
        # process the data in form.cleaned_data
        job = form.cleaned_data['job']
        country = form.cleaned_data['country']
        # here we need to pass the data to the model's methods
        job = job.replace(" ", "_").lower()
        country = country.replace(" ", "_").lower()

        active_search = Search.objects.filter(Q(job=job), Q(country=country))
        if len(active_search) > 0:
            print('add user')
            active_search[0].user.add(self.request.user)
        else:
            print('create search')
            s = Search(job=job, country=country, update_date=datetime.now(tz=timezone.utc))
            s.save()
            s.user.add(self.request.user)
        update_search(None, job=job, country=country)
        return redirect('/')

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/login')
        else:
            return super().get(request)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.accepts('text/html'):
            return response
        else:
            return JsonResponse(form.errors, status=400)