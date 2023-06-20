from django.shortcuts import redirect, render
from django.contrib import messages
# from cars_universe.accounts.models import CartItem
from cars_universe.forms import CreateToolForm, EditToolForm, DeleteToolForm, CreatePartForm, EditPartForm, \
    DeletePartForm
from cars_universe.web.models.models import CarPart, Tool, Car


def create_part(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = CreatePartForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = CreatePartForm()
        context = {
            'form': form,
        }
        return render(request, 'part_create.html', context)


def edit_part(request, pk):
    if request.user.is_staff:
        instance = CarPart.objects.get(pk=pk)
        if request.method == 'POST':
            form = EditPartForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('parts')
        else:
            form = EditPartForm(instance=instance)

        context = {
            'form': form,
            'part': instance,
        }
        return render(request, 'part_edit.html', context)


def delete_part(request, pk):
    if request.user.is_staff:
        part = CarPart.objects.get(pk=pk)
        if request.method == 'POST':
            form = DeletePartForm(request.POST, instance=part)
            if form.is_valid():
                form.save()
                return redirect('parts')
        else:
            form = DeletePartForm(instance=part)
        context = {
            'form': form,
            'part': part,
        }
        return render(request, 'part_delete.html', context)


def add_to_cart(request, item_id, item_type):
    car = False
    if item_type == 'tool':
        item = Tool.objects.get(pk=item_id)
    elif item_type == 'car_part':
        item = CarPart.objects.get(pk=item_id)
        car = True
    else:
        messages.error(request, 'Invalid item type.')
        return redirect('parts')

    cart = request.session.get('cart', {})
    if car:
        item_id += 30
    if item_id in cart:
        cart[item_id]['quantity'] += 1
        print(cart[item_id]['quantity'])
    else:
        cart_item = {
            'id': item.id,
            'name': item.name,
            'price': item.price,
            'type': item_type,
            'quantity': 1
        }
        cart[item_id] = cart_item
    request.session['cart'] = cart
    messages.success(request, 'Item added to cart.')
    if item_type == 'tool':
        return redirect('tools')
    elif item_type == 'car_part':
        return redirect('parts')


def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    if item_id in cart:
        del cart[item_id]
        request.session['cart'] = cart
    return redirect('cart')


def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('cart')


def cart_page(request):
    cart = request.session.get('cart', {})
    cart_items = []
    for item_id, item_info in cart.items():
        if item_info['type'] == 'tool':
            item = Tool.objects.get(pk=item_info['id'])
        elif item_info['type'] == 'car_part':
            item = CarPart.objects.get(pk=item_info['id'])
        else:
            continue
        quantity = item_info.get('quantity', 1)
        total_price = item.price * quantity
        cart_items.append({
            'item': item,
            'quantity': quantity,
            'total_price': total_price
        })
    #print(cart_items)
    cart_total = sum(item['total_price'] for item in cart_items)

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total
    }

    return render(request, 'cart.html', context)

