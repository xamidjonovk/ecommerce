from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.admin.views.decorators import staff_member_required
from products.models import Product  # Make sure to import your Product model
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


@api_view(['POST'])
@swagger_auto_schema(operation_description="Admin replenishes stock for a product")
@staff_member_required
def admin_replenish_stock(request, product_id, amount):
    try:
        # amount = int(request.POST.get('amount', 0))
        product = Product.objects.get(id=product_id)
        product.increase_stock(amount)

        return JsonResponse({'status': 'success', 'message': f'Successfully replenished stock by {amount}'})

    except Product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product does not exist'}, status=400)

    except ValueError:
        return HttpResponseBadRequest('Invalid input.')
