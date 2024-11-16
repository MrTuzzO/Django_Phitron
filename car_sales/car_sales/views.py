from django.shortcuts import render
from django.views.generic import DetailView
from cars.forms import CommentForm
from cars.models import Car
from brands.models import Brand


# Create your views here.
def home(request, brand_slug=None):
    data = Car.objects.all()
    brands = Brand.objects.all()
    brand_obj = None
    if brand_slug:
        brand_obj = Brand.objects.get(slug=brand_slug)
        data = Car.objects.filter(brand=brand_obj)

    return render(request, 'home.html', {'data': data, 'brands': brands, 'selected_brand': brand_obj})


class CarDetailView(DetailView):
    model = Car
    pk_url_kwarg = 'pk'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = self.object
            new_comment.save()
            comment_form = CommentForm()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        return context
