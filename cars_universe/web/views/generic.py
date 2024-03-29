

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin
from cars_universe.accounts.models import CarsUniverseUser, Profile
from cars_universe.forms import CommentForm
from cars_universe.web.models.additive_models import Event, Comment, Like
from cars_universe.web.models.models import Car, Tool, CarPart



def about(request):
    profiles = Profile.objects.all()

    context = {
        'profiles': profiles,
    }
    return render(request, 'about.html', context)


class HomeView(views.TemplateView):
    template_name = 'home_no_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = False
        return context


class DashboardView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Event
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        context['tools'] = Tool.objects.all()
        return context


class ShowEventsView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Event
    template_name = 'events.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        return context


class EventDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Event
    template_name = 'event_details.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        event = self.get_object()
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = Comment.objects.filter(event_id=event.id)
        #print(Comment.objects.filter(event_id=event.id))
        return context

    def post(self, request, *args, **kwargs):
        event = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.user = request.user
            comment.save()
            return redirect('event_details', pk=event.pk)

        context = self.get_context_data(**kwargs)
        context['comment_form'] = comment_form
        return self.render_to_response(context)


def add_comment(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, id=event_id)
        comment_text = request.POST.get('comment')
        Comment.objects.create(user=request.user, event=event, body=comment_text)
    return redirect('event details', event_id)


class ShowCarsView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Event
    template_name = 'cars.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_cars'] = Car.objects.all()
        return context


class CarDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Car
    template_name = 'car_details.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()

        return context


class ShowToolsView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Tool
    template_name = 'tools.html'
    context_object_name = 'tools'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()

        return context


class ToolDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Tool
    template_name = 'tool_details.html'
    context_object_name = 'tool'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()

        return context


class ShowPartsView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = CarPart
    template_name = 'parts.html'
    context_object_name = 'parts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parts'] = CarPart.objects.all()

        return context


class PartDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = CarPart
    template_name = 'part_details.html'
    context_object_name = 'part'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parts'] = CarPart.objects.all()

        return context




#def course(request, course_id):
 #   course_list = Course.objects.filter(courseid=course_id)
  #  enrollments_list = Enrollment.objects.filter(courseid=course_id)
   # template = loader.get_template('stadmin/course.html')
    #context = {
     #   'course': course_list[0],
      #  'enrollments': enrollments_list,
    #}

    #return HttpResponse(template.render(context, request))
